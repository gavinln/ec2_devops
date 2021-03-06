#
# puppet magic for dev boxes
#
import "classes/*.pp"

$PROJ_DIR = "/vagrant"
$HOME_DIR = "/home/vagrant"

Exec {
    path => "/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin",
}

node 'ubuntu_trusty' {
    class {
        init: ;
        python_setup:;
        # ohmyzsh_setup:;
    }
}

node 'angular' {
    class {
        init: ;
        javascript: require => Class[init];
        #python_setup:;
        #ohmyzsh_setup:;
    }
}

node 'docker' {
    hiera_include('classes')

    class {
        init: ;
        python_setup:;
        #fig_setup: require => Class[python_setup];
        ohmyzsh_setup:;
        docker_setup:;
        # docker_compose_setup: require => Class[docker_setup];
    }
}

node 'k8s' {
    class {
        init: ;
        python_setup:;
        fig_setup: require => Class[python_setup];
        ohmyzsh_setup:;
        docker_setup:;
        kubernetes_setup: require => Class[docker_setup];
    }
}

node 'caffe' {
    class {
        init: ;
        python_setup:;
        caffe_setup: require => Class[python_setup];
    }
}


node 'nltk' {
    class {
        init: ;
        python_setup:;
        nltk_setup: require => Class[python_setup];
    }
}

node 'haskell' {
    class {
        init: ;
        docker_setup:;
        docker_compose_setup: require => Class[docker_setup];
    }
}

node 'golang' {
    class {
        init: ;
        golang_setup:;
    }
}

node 'grafana' {
    class {
        init: ;
        docker_setup:;
        docker_compose_setup: require => Class[docker_setup];
        python_setup:;
        python_glances_setup: require => Class[python_setup];
        influxdb_setup:;
    }
}

node 'ansible' {
    class {
        init: ;
        ansible: ensure => master, require => Class[init];
    }
}
