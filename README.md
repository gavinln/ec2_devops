# ec2_devops
An Ubuntu 14.04 VM with Puppet, Hiera and Fabric used to setup EC2 instances on AWS

TODO add instructions here


## Start Airbnb Airflow

1. Change to the root directory

    ```
    cd ec2_devops
    ```

2. Start up the Ubuntu virtual machine

    ```
    vagrant up docker
    ```

3. Login to the virtual machine

    ```
    vagrant ssh docker
    ```

4. Change to the Docker airflow container directory

    ```
    cd /vagrant/docker/airflow/docker-airflow
    ```

5. Start up the Docker airflow container

    ```
    docker-compose up -d
    ```

6. To access Airflow UI open a browser to http://192.168.33.10:8080/

7. To access Airflow RabbitMQ interface http://192.168.33.10:15672/ with
   username/password airflow/airflow

8. To access Airflow Celery interface open a browser to http://192.168.33.10:5555/
