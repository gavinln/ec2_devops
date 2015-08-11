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
    class {
        init: ;
        python_setup:;
        fig_setup: require => Class[python_setup];
        ohmyzsh_setup:;
        docker_setup:;
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
        caffe_setup: require => Class[python_setup];
    }
}
