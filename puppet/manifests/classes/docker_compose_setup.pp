# install docker
class docker_compose_setup {
    class { 'docker_compose':
        version => '1.3.3'
    }
}


