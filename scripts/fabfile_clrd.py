from __future__ import print_function

from fabric.api import run, env, task, local
from fabric.api import cd

import os
import sys

import tasks_common as tc


script_dir = os.path.dirname(__file__)

config = tc.get_machine_config(os.path.join(script_dir, "config.yaml"))

env.user = None
env.host_string = None
env.key_filename = None


@task
def host(instance=None, ip=None):
    ''' set ec2 host '''
    tc.set_host_env(env, config, instance, ip)


@task
def start():
    ''' start ec2 instance '''
    tc.check_host_connection(env, 'start', validate_ip=False)
    instance = 'celery_redis'
    tc.start_instance(config[instance], instance)


@task
def ssh():
    ''' ssh into ec2 instance '''
    tc.check_host_connection(env, 'ssh')
    local(tc.ssh_cmd(env))


@task
def start_celery_flower():
    ''' Start Celery message queue and Flower monitory '''
    tc.check_host_connection(env, 'start_celery_flower')
    celery_redis_root = '~/ec2_devops/celery_redis'
    with cd(celery_redis_root):
        run('chmod +x *.sh')

    celery_redis_cmd = 'cd {}; ./tmux_start.sh'.format(
        celery_redis_root)
    local(tc.ssh_cmd(env, celery_redis_cmd))
