import os
import yaml
import sys

from boto.exception import EC2ResponseError

from ec2_ops import get_connection
from ec2_ops import get_only_instances
from ec2_ops import run_instances
from ec2_ops import combine_name_values
from ec2_ops import reservation_names, reservation_values
from ec2_ops import instance_names, instance_values
from ec2_ops import get_regions


script_dir = os.path.dirname(__file__)


def quote_items(items):
    return ["'{}'".format(str(item)) for item in items]


def get_machine_config(config_file):
    config = None
    with open(config_file, "r") as f:
        config = yaml.load(f)
    machine_keys = []
    for instance in config:
        key_name = config[instance]['key_name']
        if key_name != instance:
            machine_keys.append((instance, key_name))
    if len(machine_keys) > 0:
        err = 'The following machine names do not match key_name values:'
        print(err)
        err_list = []
        print('\n'.join('{} <> {}'.format(machine, key) for (
            machine, key) in machine_keys))
        sys.exit(1)
    return config


def get_tunnel_config(config_file):
    config = None
    with open(config_file, "r") as f:
        config = yaml.load(f)
    return config


def check_instance(config, instance, ip=None):
    if not instance:
        print('No instance specified')

    if instance not in config.keys():
        instances = quote_items(config.keys())
        instance_str = ', '.join(instances)
        print('instance should be one of {}'.format(instance_str))
        sys.exit(1)

    if ip not in (None, 'public'):
        print('ip should be either "public" or unspecified (default private)')


def get_key_names(config):
    ''' gets all the key_names '''
    key_names = []
    for instance in config:
        key_names.append(config[instance]['key_name'])
    return key_names


def check_host_connection(env, task_name, validate_ip=True):
    if any([env.user is None,
           env.key_filename is None]):
        msg = 'Use "host" task before the "{}" task to setup the ' \
            'host connection info'
        print(msg.format(task_name))
        sys.exit(1)

    if validate_ip and env.host_string is None:
        msg = 'No valid ip address or host name available'
        print(msg)
        sys.exit(1)


def check_tunnel(config, tunnel):
    if not tunnel:
        print('No tunnel config specified')

    if tunnel not in config.keys():
        tunnel_config = quote_items(config.keys())
        tunnel_config_str = ', '.join(tunnel_config)
        print('tunnel should be one of {}'.format(tunnel_config_str))
        sys.exit(1)


def start_instance(cfg, instance):
    conn = get_connection()
    subnet_id = cfg.get('subnet_id', None)
    reservation = run_instances(
        conn, cfg['image_id'], cfg['key_name'], cfg['instance_type'],
        cfg['security_group_ids'], subnet_id)
    print('Reservation: ' + combine_name_values(
        reservation_names(), reservation_values(reservation)))
    for instance in reservation.instances:
        print(', '.join(instance_values(instance)))


def get_ip_address(instance, key_name, ip, validate_ip=False):
    conn = get_connection()
    instances = get_only_instances(conn, filters={'key_name': instance})
    ip_address = None
    running_instances = []
    pending_instances = []
    for inst in instances:
        if inst.state == 'running':
            running_instances.append(inst)
            if ip == 'public':
                if inst.ip_address:
                    ip_address = inst.ip_address
            else:
                if inst.private_ip_address:
                    ip_address = inst.private_ip_address
            break
        elif inst.state == 'pending':
            pending_instances.append(inst)
    if validate_ip and not ip_address:
        if len(pending_instances) > 0:
            print('Pending instance of {} found'.format(instance))
        elif len(running_instances) == 0:
            print('No running instance of {} found'.format(instance))
        else:
            print('No ip address available')
    return ip_address


def set_host_env(env, config, instance, ip):
    check_instance(config, instance, ip)
    cfg_instance = config[instance]
    key_name = cfg_instance['key_name']
    pem_path = get_ssh_key(key_name)
    user = 'ubuntu'
    env.user = 'ubuntu'
    env.key_filename = pem_path

    ip_address = get_ip_address(instance, key_name, ip, validate_ip=False)
    if ip_address:
        env.hosts = [ip_address]


def get_project_name():
    ''' gets the project root directory name assuming the current
        directory is a child of the project root directory
    '''
    root_dir = os.path.normpath(os.path.join(script_dir, '..'))
    project_name = os.path.basename(root_dir)
    return project_name


def get_private_dir():
    private_dir = os.path.normpath(os.path.join(
        script_dir, '..', 'do_not_checkin'))
    return private_dir


def get_ssh_key(key_name):
    key_file = os.path.normpath(os.path.join(
        get_private_dir(), key_name + '.pem'))
    if os.path.exists(key_file):
        return key_file
    raise Exception('Key file {} does not exist'.format(key_file))


def print_instances():
    ''' print ec2 instances for default region '''
    print(', '.join(instance_names()))
    conn = get_connection()
    for instance in get_only_instances(conn):
        print(', '.join(instance_values(instance)))


def print_instances_all():
    ''' print ec2 instances for all regions '''
    regions = get_regions()
    print(', '.join(instance_names()))
    for region in regions:
        try:
            conn = get_connection(region)
            for instance in get_only_instances(conn):
                print(', '.join(instance_values(instance)))
        except EC2ResponseError:
            pass


def ssh_cmd(env, cmd=None):
    ssh_cmd = "ssh -i '{}' {}@{}".format(
        env.key_filename, env.user, env.host_string)
    if cmd:
        ssh_cmd = ssh_cmd + " -t -- '{}'".format(cmd)
    return ssh_cmd
