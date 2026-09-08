#!/bin/bash

OS_TYPE=$(uname -s)

case "$OS_TYPE" in
    Linux*)
        echo "Running on Linux"
        PROJECT_HOME=$HOME/Dev/AI-Doktora
        source $HOME/.venv/bin/activate
        python3 $PROJECT_HOME/src/Generator.py
        ;;
    Darwin*)
        echo "Running on macOS"
        PROJECT_HOME=$HOME/Dev/AI-Doktora
        source $HOME/path/to/venv/bin/activate
        python3 $PROJECT_HOME/src/Generator.py 
        # Insert Mac-specific commands here
        ;;
    *)
        echo "Unknown Operating System: $OS_TYPE"
        ;;
esac


