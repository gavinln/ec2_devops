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


