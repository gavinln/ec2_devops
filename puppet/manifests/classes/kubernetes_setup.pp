# requires docker_setup
class kubernetes_setup {
    docker::image { 'gcr.io/google_containers/etcd':
        image_tag => '2.0.9'
    }
    docker::image { 'gcr.io/google_containers/hyperkube':
        image_tag => 'v0.17.0'
    }
}


