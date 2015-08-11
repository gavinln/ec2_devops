Create configuration files for aws cli
do_not_checkin/aws.cfg
-----------------------------------
[default]
aws_access_key_id=<aws_access_key_id>
aws_secret_access_key=<aws_secret_access_key>
-----------------------------------

Create configuration file for boto
do_not_checkin/boto.cfg
-----------------------------------
[Credentials]
aws_access_key_id=<aws_access_key_id>
aws_secret_access_key=<aws_secret_access_key>
-----------------------------------

To start an ec2 instance
fab ec2_start:celery_redis

pip install pyyaml
pip install boto

conda install fabric

TODO: Should create a sqlite database that stores
1. instance.id, config.yaml (name)

1. Create a boto.cfg file in the ec2_config\do_not_checkin directory

2. cd ec2_config\scripts

3. env.bat

4. List commands
ec2 -l

5. Start ec2 instance
ec2 start:celery_redis

6. List instances
ec2 instances

7. Connect to instance
ec2 ssh

8. Connect to instance by specifying host
ec2 host:celery_redis ssh

9. Upload project to ec2
ec2 host:celery_redis upload

10. Provision machine
ec2 host:celery_redis puppet_apply

Need to solve upload issue
1. sftp
2. rsync
3. tar, gzip
4. git

To setup zsh
cd ec2_devops/scripts
chmod +x ./zsh_setup.sh
./zsh_setup.sh

Connect from Windows docker client
set DOCKER_HOST=192.168.33.10:2375
docker -H tcp://192.168.33.10:2375 ps

Make sure docker server binds to 
version => '1.6.0', # first version installed with chocolatey
tcp_bind    => 'tcp://0.0.0.0:2375',
socket_bind => 'unix:///var/run/docker.sock';

For caffe installation and instructions
https://github.com/BVLC/caffe/wiki/Ubuntu-14.04-VirtualBox-VM

Modify file below
vim Makefile.config

uncomment the line # CPU_ONLY := 1 (In a virtual machine we do not have access to the the GPU)
Under PYTHON_INCLUDE, replace /usr/lib/python2.7/dist-packages/numpy/core/include with /usr/local/lib/python2.7/dist-packages/numpy/core/include (i.e. add /local)

If you get the error: libdc1394 error: Failed to initialize libdc1394
See this: http://stackoverflow.com/questions/12689304/ctypes-error-libdc1394-error-failed-to-initialize-libdc1394
Run the following line:
sudo ln /dev/null /dev/raw1394

To run ipython notebook need the following
sudo pip install pyzmq
sudo pip install jinja2
sudo pip install tornado
sudo pip install jsonschema

