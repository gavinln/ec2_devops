set ROOT_DIR=%~dp0.

doskey ec2=fab -f %ROOT_DIR%\fabfile.py $*
set BOTO_CONFIG=%ROOT_DIR%\..\do_not_checkin\boto.cfg
set EC2_REGION=us-west-1
