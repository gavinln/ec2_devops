from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd

from fabric.utils import abort


import os
import shutil
import sys

from StringIO import StringIO


script_dir = os.path.dirname(__file__)


def get2():
    ' get list of pods '
    kube = os.path.join(script_dir, 'kubectl')
    out = local('{} get pods'.format(kube), capture=True)
    fh = StringIO()
    for line in StringIO(out).readlines():
        if line.find('gcr.io/google_containers/hyperkube') == -1:
            print('{}'.format(line), end='')


@task
def pods():
    ' get list of pods '
    kube = os.path.join(script_dir, 'kubectl')
    local('{} get pods -l run-container=nginx'.format(kube))


@task
def services():
    ' get list of services'
    kube = os.path.join(script_dir, 'kubectl')
    local('{} get services nginx'.format(kube))


@task
def rc():
    ' get list of services'
    kube = os.path.join(script_dir, 'kubectl')
    local('{} get rc nginx'.format(kube))


@task
def resize(count=None):
    ' resize replication controllers '
    if count is None:
        abort('No count specified. Should be a number')
    kube = os.path.join(script_dir, 'kubectl')
    local('{} resize --replicas={} rc nginx'.format(
        kube, count))


possible_status = (
    'restarting',
    'running',
    'paused',
    'exited')


def check_status(status):
    if status not in possible_status:
        status_str = ', '.join(possible_status)
        print('status should be one of {}'.format(status_str))
        sys.exit(1)


@task
def ps(status=None):
    ' get list of docker containers by status '
    if status:
        check_status(status)
        local('docker ps -a -f status={}'.format(status))
    else:
        local('docker ps -a')
