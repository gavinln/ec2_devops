# install python glances
class python_glances_setup {
    case $operatingsystem {
        ubuntu: {
            package { 'glances':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'bottle':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'influxdb':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
