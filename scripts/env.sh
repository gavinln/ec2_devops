#!/bin/bash
#
# Usage: source env.sh

DEPLOY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export AWS_CONFIG_FILE=/vagrant/do_not_checkin/aws.cfg
export BOTO_CONFIG=/vagrant/do_not_checkin/boto.cfg
export EC2_REGION=us-west-2

function ec2-fabfile() {
  fab -f $DEPLOY_DIR/fabfile.py $*
}

alias ec2='ec2-fabfile'
