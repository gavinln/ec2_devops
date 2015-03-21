set ROOT_DIR=%~dp0.

doskey ec2=fab -f %ROOT_DIR%\fabfile_ec2.py $*
doskey clrd=fab -f %ROOT_DIR%\fabfile_clrd.py $*

set BOTO_CONFIG=%ROOT_DIR%\..\do_not_checkin\boto.cfg
set EC2_REGION=us-west-2
