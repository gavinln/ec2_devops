#!/bin/bash
#
# Usage: source env.sh

DEPLOY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export AWS_CONFIG_FILE=/vagrant/do_not_checkin/aws.cfg
export BOTO_CONFIG=/vagrant/do_not_checkin/boto.cfg

function system-info() {
  fab -f $DEPLOY_DIR/fabfile.py $*
}

alias si='system-info'
alias si-host-type='system-info host-type'
alias si-ssh-config='system-info ssh-config'

