# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  
#  config.vm.provision :shell,
#    :inline => 'echo "America/Los_Angeles" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata'

  # do not update configured box
  config.vm.box_check_update = false

  # user insecure key
  config.ssh.insert_key = false

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  config.ssh.forward_x11 = true

  config.ssh.forward_agent = true

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true

    # Customize the amount of memory on the VM:
    vb.memory = "4096"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: $script
  config.vm.provision "shell", path: 'puppet/install_puppet_modules.sh'

  config.vm.define :ubuntu_trusty, autostart: false do |machine|
    machine.vm.network "forwarded_port", guest: 22, host: 2200
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :ubuntu_trusty
      # puppet.hiera_config_path = "hiera.yaml"
      # puppet.options = "--verbose --debug"
    end
  end

  config.vm.define :angular, autostart: false do |machine|
    machine.vm.provision "puppet" do |puppet|
      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :angular
    end
  end

  config.vm.define :docker, autostart: false do |machine|
    machine.vm.hostname = :docker
    machine.vm.network "forwarded_port", guest: 2375, host: 2375
    machine.vm.provision "puppet" do |puppet|
      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s --reports store --hiera_config=/vagrant/hiera.yaml" % :docker
    end
  end

  config.vm.define :k8s, autostart: false do |machine|
    machine.vm.hostname = "k8s"
    machine.vm.network "forwarded_port", guest: 2375, host: 2375
    machine.vm.provision "puppet" do |puppet|
      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :k8s
      # puppet.options = "--verbose --debug"
    end
  end

  config.vm.define :caffe, autostart: false do |machine|
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :caffe
    end
  end

  config.vm.define :nltk, autostart: false do |machine|
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :nltk
    end
  end

  config.vm.define :haskell, autostart: false do |machine|
    machine.vm.hostname = :haskell
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :haskell
    end
  end

  config.vm.define :golang, autostart: false do |machine|
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :golang
    end
  end

  config.vm.define :ansible, autostart: false do |machine|
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :ansible
    end
  end


  config.vm.define :grafana, autostart: false do |machine|
    machine.vm.network :forwarded_port, guest: 8083, host: 8083  # influxdb web
    machine.vm.network :forwarded_port, guest: 8086, host: 8086  # influxdb port - may need to remove
    machine.vm.network :forwarded_port, guest: 3000, host: 3000  # grafana port

    machine.vm.hostname = :grafana
    machine.vm.provision "puppet" do |puppet|

      puppet.manifest_file  = "default.pp"
      puppet.manifests_path = "puppet/manifests"
      puppet.options = "--certname=%s" % :grafana
    end
  end
end
