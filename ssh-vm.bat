@echo off

set KEY_FILE=~/.ssh/id_rsa
bash -c "eval `ssh-agent`; ssh-add; vagrant ssh ansible -- -t '. /etc/profile; bash -l'"

REM bash -c "eval `ssh-agent`; ssh-add; vagrant ssh vm -- -t '. /etc/profile; cd /srv/share; bash'"
