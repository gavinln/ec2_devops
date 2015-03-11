set ROOT_DIR=%~dp0.

doskey ec2=fab -f %ROOT_DIR%\fabfile.py $*
