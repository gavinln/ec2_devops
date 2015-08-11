# install caffe
# depends on python_setup.pp
class caffe_setup {
    case $operatingsystem {
        ubuntu: {
            package { 'numpy':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'scipy':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'matplotlib':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'ipython':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'pandas':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            $caffe_packages = [
                'libprotobuf-dev', 'libleveldb-dev', 'libsnappy-dev',
                'libopencv-dev', 'libboost-all-dev', 'libhdf5-serial-dev',
                'protobuf-compiler', 'gfortran', 'libjpeg62',
                'libfreeimage-dev', 'libatlas-base-dev',
                'libgoogle-glog-dev', 'libbz2-dev', 'libxml2-dev',
                'libxslt-dev', 'libffi-dev', 'libssl-dev', 'libgflags-dev',
                'liblmdb-dev']
            package { $caffe_packages :
                ensure => installed
            }
            # cython has to be installed before h5py
            package { 'cython':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'h5py':
                ensure => installed,
                provider => pip,
                require => Package['cython']
            }
            package { ['leveldb', 'networkx', 'protobuf',
                'python-gflags', 'pyyaml', 'scikit-image']:
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'Pillow':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
