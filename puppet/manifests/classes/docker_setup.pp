# install docker
class docker_setup {
    class { 'docker':
        version => '1.6.0',
        tcp_bind    => 'tcp://0.0.0.0:2375',
        socket_bind => 'unix:///var/run/docker.sock';
    }
    user {'vagrant':
        ensure => 'present'
    }
    exec {"vagrant_in_docker":
      unless => "grep -q 'docker\\S*vagrant' /etc/group",
      command => "usermod -aG docker vagrant",
      require => [User['vagrant'], Class['docker']]
    }
}


