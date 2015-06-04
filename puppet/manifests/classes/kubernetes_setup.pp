# requires docker_setup
class kubernetes_setup {
    docker::image { 'gcr.io/google_containers/etcd':
        image_tag => '2.0.9'
    }
    docker::image { 'gcr.io/google_containers/hyperkube':
        image_tag => 'v0.17.0'
    }
    wget::fetch { 'kubectl':
        source => "https://storage.googleapis.com/kubernetes-release/release/v0.17.0/bin/linux/amd64/kubectl",
        destination => "/tmp/kubectl"
    } ->
    file { '/usr/bin/kubectl':
        mode => 0755,
        source => '/tmp/kubectl'
    } ->
    wget::fetch { 'kubectl_bash':
        source => "https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes/4ba22e713ad95dfb308d0b9aca7ac9d980414bf6/contrib/completions/bash/kubectl",
        destination => "/etc/bash_completion.d/kubectl"
    }
}


