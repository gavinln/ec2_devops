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


