# install python
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { "python-dev":
                ensure => installed
            }
            package { "python-pip":
                ensure => installed,
                require => Package['python-dev']
            }
            package { 'fabric':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'boto':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'awscli':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
