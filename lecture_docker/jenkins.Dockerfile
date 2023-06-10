FROM jenkins/jenkins:lts

COPY install_allure.py /home/install_allure.py

USER root

RUN apt-get update -y
RUN apt-get install vim docker.io -y

USER jenkins
