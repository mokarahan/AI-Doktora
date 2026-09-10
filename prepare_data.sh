#!/bin/bash

OS_TYPE=$(uname -s)

PROJECT_HOME=$HOME/Dev/AI-Doktora
EXDIR=$PROJECT_HOME/export

if [[ -d "$EXDIR" ]]; then
    echo "$EXDIR exists."
else
    echo "$EXDIR does not exist."
    mkdir -p "$DIR"
fi

case "$OS_TYPE" in
    Linux*)
        echo "Running on Linux"
        source $HOME/.venv/bin/activate
        python3 $PROJECT_HOME/src/Generator.py
        ;;
    Darwin*)
        echo "Running on macOS"
        source $HOME/path/to/venv/bin/activate
        python3 $PROJECT_HOME/src/Generator.py 
        ;;
    *)
        echo "Unknown Operating System: $OS_TYPE"
        ;;
esac


