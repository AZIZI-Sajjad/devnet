FROM debian:bullseye

RUN apt-get update && apt upgrade -y \
&& which git || apt install git -y \
apt install curl net-tools iputils-ping traceroute dnsutils iputils-ping openssh-server -y \
&& apt-get clean -y

# ADD . /devicebackup/
WORKDIR /devicebackup
# RUN npm install

