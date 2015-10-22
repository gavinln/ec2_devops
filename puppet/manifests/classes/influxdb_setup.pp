# install influxdb
class influxdb_setup {
    case $operatingsystem {
        ubuntu: {
            class {'influxdb::server':}
        }
    }
}
