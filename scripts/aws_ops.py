from __future__ import print_function

from fabric.api import run, env, task, roles, local, lcd

import os
import shutil
import datetime as dt

from boto import ec2
import os


def get_connection():
    conn = ec2.connect_to_region(
        'us-west-1',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    return conn

my_code = """#!/bin/bash

apt-get install puppet-common -y

"""


def run_instance(conn, image_id, key_name, instance_type):
    reservation = conn.run_instances(
        image_id=image_id,
        key_name=key_name,
        instance_type=instance_type,
        security_group_ids=[os.environ['SECURITY_GROUP_ID']],
        subnet_id=os.environ['SUBNET_ID'],
        instance_initiated_shutdown_behavior='terminate',
        user_data=my_code)
    return reservation


def get_instances(reservation):
    return [instance.id for instance in reservation.instances]


def quote_items(items):
    return ["'{}'".format(str(item)) for item in items]


def instance_attrs():
    return ['id', 'instance_type', 'state', 'image_id', 'private_ip_address',
            'key_name', 'launch_time', 'Name']


def instance_values(instance):
    values = [instance.__getattribute__(
        attribute) for attribute in instance_attrs()[:-1]]

    def blank_if_none(item):
        return item if item else ''

    values = [blank_if_none(item) for item in values]

    launch_time = values[-1]
    launch_time_delta = str(dt.datetime.utcnow() - dt.datetime.strptime(
        launch_time, '%Y-%m-%dT%H:%M:%S.%fZ'))
    # remove seconds and comma
    last_dot = launch_time_delta.rfind('.')
    values[-1] = launch_time_delta[:last_dot].replace(',', '')
    if 'Name' in instance.tags:
        values.append(instance.tags['Name'])
    else:
        values.append('')
    return values


def print_reservation(reservation):
    print('Reservation: {}'.format(reservation.id))
    instances = quote_items(get_instances(reservation))
    instances_str = ', '.join(instances)
    print('\tInstances: [{}]'.format(instances_str))


def get_all_instances(conn):
    reservations = conn.get_all_instances(
            filters={'subnet-id': 'subnet-0fca106a'})
    instances = []
    for reservation in reservations:
        instances.extend(get_instances(reservation))
    return instances


def get_only_instances(conn, filters=None):
    return conn.get_only_instances(filters=filters)


def find_instance_by_key_name(conn, key_name):
    for instance in conn.get_only_instances():
        if instance.key_name == key_name:
            return instance
    return None


def stop_instances(conn):
    instances = get_all_instances(conn)
    for instance in instances:
        conn.stop_instances(instance)


def terminate_instances(conn):
    instances = get_all_instances(conn)
    for instance in instances:
        conn.terminate_instances(instance)
