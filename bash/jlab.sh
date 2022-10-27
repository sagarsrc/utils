#!/bin/bash

# script for tunneling jupyter lab from ec2 instance to local
# bash jlab.sh


# port on which jupyter lab is running on ec2
remote_port="8888"

# port on which you want to access jupyter lab on your local machine
local_port="8888"

# you can automate your password prompt using sshpass
sshpass -p 'yourpass' ssh -i ~/.ssh/secret.pem  -NL $remote_port:localhost:$port username@machine &

# if password prompt is not required use this
# ssh -i ~/.ssh/secret.pem  -NL $remote_port:localhost:$port username@machine &

sleep 5
echo "runing jupyterlab at http://localhost:$local_port/lab/"