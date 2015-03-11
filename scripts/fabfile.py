from __future__ import print_function

from fabric.api import run, env, task, roles, local, lcd
import os
import shutil
import yaml
import sys

from aws_ops import run_instance
from aws_ops import get_connection
from aws_ops import stop_instances
from aws_ops import terminate_instances
from aws_ops import quote_items
from aws_ops import get_only_instances

from aws_ops import instance_names
from aws_ops import instance_values

from aws_ops import reservation_names
from aws_ops import reservation_values

from aws_ops import combine_name_values

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "config.yaml"), "r") as f:
    config = yaml.load(f)


def check_instance(config, instance):
    if not instance:
        print('No instance specified')

    if instance not in config.keys():
        instances = quote_items(config.keys())
        instance_str = ', '.join(instances)
        print('instance should be one of {}'.format(instance_str))
        sys.exit(1)


@task
def start(instance=None):
    ''' start ec2 instance '''
    check_instance(config, instance)
    conn = get_connection()
    cfg_instance = config[instance]
    reservation = run_instance(
        conn, cfg_instance['image_id'], cfg_instance['key_name'],
        cfg_instance['instance_type'])
    print(combine_name_values(reservation_names(), reservation_values(
      reservation)))
    for instance in reservation.instances:
        print(', '.join(instance_values(instance)))


@task
def terminate():
    ''' terminate ec2 instances '''
    conn = get_connection()
    terminate_instances(conn)


@task
def ssh(instance=None):
    ''' ssh into instance - not working '''
    check_instance(config, instance)
    cfg_instance = config[instance]
    pem_path = os.path.normpath(os.path.join(
        script_dir, '..', 'do_not_checkin',
        cfg_instance['key_name'] + '.pem'))

    conn = get_connection()
    instances = get_only_instances(
            conn, filters={'key_name': instance})
    ip_address = None
    instance_running = False
    for inst in instances:
        if inst.state == 'running':
            instance_running = True
            if inst.private_ip_address:
                ip_address = inst.private_ip_address
            break
    if ip_address:
        local('ssh -i "{}" ubuntu@{}'.format(pem_path, ip_address))
    elif instance_running is False:
        print('No running instance of {} found'.format(instance))
    else:
        print('No private ip address available')


@task
def instances():
    ''' get ec2 instances '''
    conn = get_connection()
    print(', '.join(instance_names()))
    for instance in get_only_instances(conn):
        print(', '.join(instance_values(instance)))
