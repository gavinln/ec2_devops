FROM tomcat:7.0

MAINTAINER Gavin Noronha <gavinln@hotmail.com>

WORKDIR /usr/local/tomcat

RUN cp $CATALINA_HOME/webapps/docs/appdev/sample/sample.war $CATALINA_HOME/webapps

CMD ["bin/catalina.sh", "run"]
