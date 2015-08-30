#!/bin/bash

# Exit on any errors.
set -e

PUPPET_INSTALL='puppet module install --module_repository http://forge.puppetlabs.com'

# install puppet modules
(puppet module list | grep acme-ohmyzsh) ||
    $PUPPET_INSTALL -v 0.1.2 acme-ohmyzsh

(puppet module list | grep garethr-docker) ||
    $PUPPET_INSTALL -v 4.0.2 garethr-docker

(puppet module list | grep willdurand-nodejs) ||
    $PUPPET_INSTALL -v 1.8.3 willdurand-nodejs

(puppet module list | grep maestrodev-wget) ||
    $PUPPET_INSTALL -v 1.7.0 maestrodev-wget

# (puppet module list | grep puppetlabs-reboot) ||
#     $PUPPET_INSTALL -v 1.1.0 puppetlabs-reboot
# 
# (puppet module list | grep wilrnh-cuda) ||
#     $PUPPET_INSTALL -v 0.1.0 wilrnh-cuda

(puppet module list | grep garystafford-docker_compose) ||
    $PUPPET_INSTALL -v 0.2.2 garystafford-docker_compose



