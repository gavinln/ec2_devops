# install python
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { "python-pip":
                ensure => installed
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
