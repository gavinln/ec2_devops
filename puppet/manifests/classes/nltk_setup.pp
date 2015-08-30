# install nltk
# depends on python_setup.pp
class nltk_setup {
    case $operatingsystem {
        ubuntu: {
            package { 'numpy':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'pyyaml':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'nltk':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
