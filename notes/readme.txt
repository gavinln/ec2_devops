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
