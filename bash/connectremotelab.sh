#!/bin/bash

# script for tunneling jupyter lab from ec2 instance to local


# remote details
remote_port="8890"
username="ubuntu"
machine="11.22.33.44"


# local details
local_port="8899"

# you can automate your password prompt using sshpass
## if password
# sshpass -p 'yourpass' ssh -i ~/.ssh/secret.pem  -NL $remote_port:localhost:$port username@machine &
## if not password
cmd='ssh -i ~/.ssh/secret.pem  -NL $remote_port:localhost:$local_port $username@$machine &'
echo "running $(eval echo "$cmd")"

# run command
eval $cmd

sleep 5
echo "runing jupyterlab at http://localhost:$local_port/lab/"