#!/bin/bash

# Check if the Tmux session exists
if ! tmux has-session -t jupyter_session 2>/dev/null; then
  # Start a new Tmux session
    tmux new-session -d -s jupyter_session

    # Start a Jupyter Notebook within the Tmux session
    tmux send-keys "jupyter-lab --port=8890 --no-browser" C-m

    # Attach to the Tmux session to view the notebook
    # tmux attach-session -t jupyter_session
else
  echo "[INFO] jupyter-lab running on port 8890"
fi