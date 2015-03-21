from __future__ import print_function

from fabric.api import run, env, task, roles, local, lcd

import os
import shutil
import datetime as dt

from boto import ec2
import os
import sys
import tasks_common as tc


def get_regions():
    regions = []
    for region in ec2.regions():
        regions.append(region.name)
    return regions


def get_connection(region=None):
    ''' if no region is specifed uses the EC2_REGION variable '''
    if region is None:
        region_key = 'EC2_REGION'
        if region_key not in os.environ:
            print('Environment variable {} not set'.format(
                region_key))
            sys.exit(1)

        ec2_region = os.environ['EC2_REGION']
    else:
        ec2_region = region

    conn = ec2.connect_to_region(ec2_region)
    return conn


my_code = """#!/bin/bash

apt-get install puppet-common -y

"""


def run_instances(conn, image_id, key_name, instance_type,
                  security_group_ids, subnet_id):
    ec2_region = os.environ['EC2_REGION']
    ec2 = {
        'region': ec2_region, 'image_id': image_id, 'key_name': key_name,
        'instance_type': instance_type,
        'security_group_ids': security_group_ids,
        'subnet_id': subnet_id
    }
    print('Run instances: ' + combine_name_values(ec2.keys(), ec2.values()))
    reservation = conn.run_instances(
        image_id=image_id,
        key_name=key_name,
        instance_type=instance_type,
        security_group_ids=security_group_ids,
        subnet_id=subnet_id,
        instance_initiated_shutdown_behavior='terminate',
        user_data=my_code, dry_run=False)
    return reservation


def get_instances(reservation):
    return [instance.id for instance in reservation.instances]


# TODO: move to common file
def combine_name_values(names, values, sep='=', attr_sep=', '):
    name_values = [(name, value) for name, value in zip(
        names, values)]
    return attr_sep.join("{}{}{}".format(
        name, sep, value) for name, value in name_values)


def reservation_names():
    return ['id', 'region', 'owner_id']


def reservation_values(reservation):
    values = [reservation.__getattribute__(
        attribute) for attribute in reservation_names()]
    return values


def instance_names():
    return ['region', 'id', 'instance_type', 'state', 'image_id',
            'key_name', 'ip_address', 'private_ip_address', 'launch_time',
            'Name']


def instance_values(instance):
    values = [instance.__getattribute__(
        attribute) for attribute in instance_names()[:-1]]

    # convert RegionInfo to string
    values[0] = values[0].name

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
    filters = {'instance_type': 't2.medium'}
    instances = get_only_instances(conn, filters=filters)
    for instance in instances:
        conn.terminate_instances(instance.id)
    return len(instances)
