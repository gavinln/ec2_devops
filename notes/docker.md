## To use Docker without sudo
sudo gpasswd -a ${USER} docker

## For the IPython tmpnb server
docker pull jupyter/demo
docker pull jupyter/minimal

export TOKEN=$( head -c 30 /dev/urandom | xxd -p )

docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=proxy jupyter/configurable-http-proxy --default-target http://127.0.0.1:9999

docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN \
    --name=tmpnb -v /var/run/docker.sock:/docker.sock jupyter/tmpnb

docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN -v /var/run/docker.sock:/docker.sock jupyter/tmpnb python orchestrate.py --image='jupyter/demo'

docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN -v /var/run/docker.sock:/docker.sock jupyter/tmpnb python orchestrate.py --image='jupyter/demo' --command="ipython3 notebook --NotebookApp.base_url={base_path} --ip=0.0.0.0 --port {port}" 
