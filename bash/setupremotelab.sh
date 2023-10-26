# add this to .remotelab.sh in remote
echo "jupyter-lab --port=8890 --no-browser" > ~/.remotelab.sh

# add alias in .bashrc to run this file
echo 'alias remotelab="bash /home/ubuntu/.remotelab.sh"' >> ~/.bash_aliases