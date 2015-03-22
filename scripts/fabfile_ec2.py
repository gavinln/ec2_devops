from __future__ import print_function

from fabric.api import run, env, task, roles, local, lcd
from fabric.api import open_shell, put, cd, sudo
from fabric.api import settings
from fabric import network
from fabric.context_managers import remote_tunnel
from fabric.state import connections

from fabric.contrib import files

import os
import shutil
import yaml
import sys

import tasks_common as tc

from ec2_ops import get_connection
from ec2_ops import get_only_instances

from ec2_ops import stop_instances
from ec2_ops import terminate_instances


script_dir = os.path.dirname(__file__)

# TODO: rename config.yaml to machine.yaml ???
config = tc.get_machine_config(os.path.join(script_dir, "config.yaml"))
tunnel_config = tc.get_tunnel_config(os.path.join(script_dir, "tunnel.yaml"))


env.user = None
env.host_string = None
env.key_filename = None


def local_tunnel_ssh(env, local_port, remote_host, remote_port):
    return local('ssh -L {0}:{1}:{2} -i "{3}" {4}@{5}'.format(
        local_port, remote_host, remote_port,
        env.key_filename, env.user, env.host_string))


@task
def start(instance=None):
    ''' start ec2 instance '''
    tc.check_instance(config, instance)
    cfg = config[instance]
    tc.start_instance(cfg, instance)


@task
def terminate():
    ''' terminate ec2 instances '''
    conn = get_connection()
    instance_count = terminate_instances(conn, tc.get_key_names(config))
    print('Terminated {} instances'.format(instance_count))


@task
def ssh():
    ''' ssh into ec2 instance '''
    tc.check_host_connection(env, 'ssh')
    local(tc.ssh_cmd(env))


@task
def instances():
    ''' print ec2 instances for default region '''
    tc.print_instances()


@task
def instances_all():
    ''' print ec2 instances for all regions '''
    tc.print_instances_all()


@task
def host(instance=None, ip=None):
    ''' set ec2 host '''
    tc.set_host_env(env, config, instance, ip)


@task
def upload():
    ''' upload project to a ec2 instance '''
    tc.check_host_connection(env, 'upload')
    project_name = tc.get_project_name()
    root_dir = os.path.normpath(os.path.join(script_dir, '..'))
    dest_name = '~/' + project_name

    run('mkdir -p {}'.format(dest_name))

    files = os.listdir(root_dir)
    ignore_files = ['.git', '.vagrant', 'do_not_checkin']
    for filename in files:
        if filename not in ignore_files:
            local_file = os.path.join(root_dir, filename)
            put(local_file, dest_name)


@task
def provision():
    ''' install puppet modules & runs manifests '''
    tc.check_host_connection(env, 'provision')
    project_name = tc.get_project_name()
    project_root = '~/' + project_name
    if not files.exists(project_root):
        print('Project {} does not exist in host {}'.format(
            project_root, project_name))
    else:
        with cd(project_root):
            run('chmod +x ./puppet/install_puppet_modules.sh')
            sudo('./puppet/install_puppet_modules.sh')
            vm_name, ext = os.path.splitext(os.path.basename(env.key_filename))
            cmd = 'puppet apply --certname={} puppet/manifests/default.pp'
            sudo(cmd.format(vm_name))


@task
def copy_private_key(key_name=None):
    ''' get network keys '''
    ''' ssh-keygen -f gitlab.rsa -t rsa -N '' '''
    tc.check_host_connection(env, 'copy_private_key')
    key_file = None
    if key_name is None:
        print('No key_name specified')
        sys.exit(1)
    else:
        key_file = os.path.normpath(os.path.join(
            get_private_dir(), key_name))
        if not os.path.exists(key_file):
            print('Key file {} does not exist'.format(key_file))
            sys.exit(1)

    ssh_root = '~/.ssh'
    print('Testing where {} exists'.format(ssh_root))
    if files.exists(ssh_root):
        put(key_file, remote_path=ssh_root)
        remote_key_file = ssh_root + '/' + key_name
        # run('chmod 400 {}'.format(remote_key_file))


@task
def rtunnel(tunnel=None):
    ' make a locally-visible port accessible remotely'
    tc.check_host_connection(env, 'rtunnel')
    tc.check_tunnel(tunnel_config, tunnel)
    config = tunnel_config[tunnel]
    with remote_tunnel(config['remote'], local_port=config['local'],
                       local_host=config['domain']):
        local(tc.ssh_cmd(env))


@task
def ltunnel(tunnel=None):
    ' make a remotely-visible port accessible locally'
    tc.check_host_connection(env, 'ltunnel')
    tc.check_tunnel(tunnel_config, tunnel)
    config = tunnel_config[tunnel]
    local_tunnel_ssh(env, config['local'], config['domain'],
                     config['remote'])
