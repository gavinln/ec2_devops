#
# puppet magic for dev boxes
#
import "classes/*.pp"

$PROJ_DIR = "/vagrant"
$HOME_DIR = "/home/vagrant"

Exec {
    path => "/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin",
}

node 'celery_redis' {
    class {
        init: ;
        #python_setup:;
        #ohmyzsh_setup:;
    }
    notify { 'Hello World celery_redis': }
}

node 'angular' {
    class {
        init: ;
        javascript: require => Class[init];
        #python_setup:;
        #ohmyzsh_setup:;
    }
    notify { 'Hello World other': }
}




