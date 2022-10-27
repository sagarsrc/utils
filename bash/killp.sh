#!/bin/bash

# kill process running at port
# bash killp 8887

kill -9 $(lsof -t -i:$1)
