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

(puppet module list | grep saz-timezone) ||
    $PUPPET_INSTALL -v 3.3.0 saz-timezone

(puppet module list | grep garystafford-docker_compose) ||
    $PUPPET_INSTALL -v 0.2.2 garystafford-docker_compose

(puppet module list | grep saz-dnsmasq) ||
    $PUPPET_INSTALL -v 1.2.0 saz-dnsmasq

(puppet module list | grep golja-influxdb) ||
    $PUPPET_INSTALL -v 1.1.0 golja-influxdb

(puppet module list | grep dcoxall-golang) ||
    $PUPPET_INSTALL -v 1.1.1 dcoxall-golang
