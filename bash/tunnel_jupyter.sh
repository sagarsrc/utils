#!/bin/bash

# Remote details
remote_port="88RR"
username="ubuntu"
machine="20.20.20.20"
local_port="88LL"
pem_file="~/.ssh/secret.pem"
# echo "ssh -i $pem_file  -NfL $local_port:localhost:$remote_port $username@$machine"

# figlet -f larry3d Jupyter

# working command
# ssh -i ~/.ssh/secret.pem  -L 88LL:localhost:88RR ubuntu@20.2.72.108

Check if the local port is in use
if ! nc -z localhost $local_port; then
  # If the local port is available, start a new Tmux session
  tmux new-session -d -s jupyter_tunnel

  # Establish an SSH tunnel within the Tmux session using the PEM file
  tmux send-keys "ssh -i $pem_file  -NL $local_port:localhost:$remote_port $username@$machine" C-m

  echo "[INFO] jupyter <===> remote-machine"
  echo "[INFO] SSH tunnel to remote Jupyter Notebook established in a Tmux session."
  echo "[INFO] You can access it locally at http://localhost:$local_port"

  # tmux attach-session -t jupyter_tunnel
else
  echo "[ERROR] Local port $local_port is already in use."
fi


