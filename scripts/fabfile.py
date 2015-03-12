'''
TODO: May need to fix error in
http://askubuntu.com/questions/59458/error-message-when-i-run-sudo-unable-to-resolve-host-none
'''
from __future__ import print_function

from fabric.api import run, env, task, roles, local, lcd
from fabric.api import open_shell, put, cd, sudo
from fabric.api import settings

from fabric.contrib.files import exists

import os
import shutil
import yaml
import sys

from aws_ops import get_connection
from aws_ops import get_only_instances

from aws_ops import run_instance
from aws_ops import stop_instances
from aws_ops import terminate_instances
from aws_ops import quote_items

from aws_ops import instance_names, instance_values
from aws_ops import reservation_names, reservation_values

from aws_ops import combine_name_values

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "config.yaml"), "r") as f:
    config = yaml.load(f)

env.user = None
env.host_string = None
env.key_filename = None


def check_instance(config, instance):
    if not instance:
        print('No instance specified')

    if instance not in config.keys():
        instances = quote_items(config.keys())
        instance_str = ', '.join(instances)
        print('instance should be one of {}'.format(instance_str))
        sys.exit(1)


def check_host_connection(task_name):
    if any([env.user is None,
           env.host_string is None,
           env.key_filename is None]):
        msg = 'Use "host" task before the "{}" task to setup the ' \
            'host connection info'
        print(msg.format(task_name))
        sys.exit(1)


def get_project_name():
    ''' gets the project root directory name assuming the current
        directory is a child of the project root directory
    '''
    root_dir = os.path.normpath(os.path.join(script_dir, '..'))
    project_name = os.path.basename(root_dir)
    return project_name


@task
def start(instance=None):
    ''' start ec2 instance '''
    check_instance(config, instance)
    conn = get_connection()
    cfg_instance = config[instance]
    reservation = run_instance(
        conn, cfg_instance['image_id'], cfg_instance['key_name'],
        cfg_instance['instance_type'], cfg_instance['security_group_ids'])
    print(combine_name_values(reservation_names(), reservation_values(
        reservation)))
    for instance in reservation.instances:
        print(', '.join(instance_values(instance)))


@task
def terminate():
    ''' terminate ec2 instances '''
    conn = get_connection()
    terminate_instances(conn)


def get_ssh_key(key_name):
    key_file = os.path.normpath(os.path.join(
        script_dir, '..', 'do_not_checkin', key_name + '.pem'))
    if os.path.exists(key_file):
        return key_file
    raise Exception('Key file {} does not exist'.format(key_file))


def get_ip_address(instance, key_name):
    conn = get_connection()
    instances = get_only_instances(conn, filters={'key_name': instance})
    ip_address = None
    running_instances = []
    pending_instances = []
    for inst in instances:
        if inst.state == 'running':
            running_instances.append(inst)
            if inst.private_ip_address:
                ip_address = inst.private_ip_address
            break
        elif inst.state == 'pending':
            pending_instances.append(inst)
    if not ip_address:
        if len(pending_instances) > 0:
            print('Pending instance of {} found'.format(instance))
        elif len(running_instances) == 0:
            print('No running instance of {} found'.format(instance))
        else:
            print('No private ip address available')
    return ip_address


@task
def shell():
    ''' ssh into ec2 instance - does not work properly '''
    check_host_connection('shell')
    open_shell('export TERM=ansi')


@task
def ssh():
    ''' ssh into ec2 instance '''
    check_host_connection('ssh')
    local('ssh -i "{}" {}@{}'.format(
        env.key_filename, env.user, env.host_string))


@task
def instances():
    ''' get ec2 instances '''
    conn = get_connection()
    print(', '.join(instance_names()))
    for instance in get_only_instances(conn):
        print(', '.join(instance_values(instance)))


@task
def host(instance=None):
    ''' set ec2 host '''
    check_instance(config, instance)
    cfg_instance = config[instance]
    key_name = cfg_instance['key_name']
    ip_address = get_ip_address(instance, key_name)
    pem_path = get_ssh_key(key_name)
    user = 'ubuntu'
    if ip_address:
        # print('Setting host: {}@{}'.format(user, ip_address))
        # print('Setting key_file: {}'.format(pem_path))
        env.user = 'ubuntu'
        env.hosts = [ip_address]
        env.key_filename = pem_path


@task
def upload():
    ''' upload project to a ec2 instance '''
    check_host_connection('upload')
    root_dir = os.path.normpath(os.path.join(script_dir, '..'))
    project_name = os.path.basename(root_dir)
    dest_name = '~/' + project_name

    run('mkdir -p {}'.format(dest_name))

    files = os.listdir(root_dir)
    ignore_files = ['.git', '.vagrant', 'do_not_checkin']
    for filename in files:
        if filename not in ignore_files:
            local_file = os.path.join(root_dir, filename)
            put(local_file, dest_name)


@task
def puppet_apply():
    ''' install puppet modules & runs manifests '''
    check_host_connection('puppet_apply')
    project_name = get_project_name()
    project_root = '~/' + project_name
    if not exists(project_root):
        print('Project {} does not exist of host {}'.format(
            project_root, project_name))
    else:
        with cd(project_root):
            run('chmod +x ./puppet/install_puppet_modules.sh')
            sudo('./puppet/install_puppet_modules.sh')
            sudo('puppet apply puppet/manifests/default.pp')
