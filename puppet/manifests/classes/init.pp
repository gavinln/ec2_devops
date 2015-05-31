# Commands to run before all others in puppet.
class init {
    $git_cmd = "git config --global"
    group { "puppet":
        ensure => "present",
    }
    case $operatingsystem {
        ubuntu: {
            exec { "update_apt":
                command => "sudo apt-get update",
            }
            Exec["update_apt"] -> Package <| |>
            $misc_packages = ['git-core', 'tmux']
            package { $misc_packages:
                ensure => present,
            }
            package { 'autojump':
                ensure => present,
                require => Exec['update_apt'];
            }
            file { '/etc/profile.d/autojump.sh':
                ensure => present,
                source => '/usr/share/autojump/autojump.sh',
                require => Package['autojump']
            }
# does not work as it raises and error
#            exec { 'update_autojump':
#                command => 'autojump -a /vagrant',
#                environment => "HOME=/home/vagrant",
#                user => "vagrant",
#                require => Package['autojump'];
#            }
        }
    }
}
