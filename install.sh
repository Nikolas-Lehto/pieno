#!/bin/bash

    echo '---------------------------------------|  Pieno installer 1.3  |---------------------------------------'

if [ ! -d venv ]; then
    echo "No Python virtual environment in this directory.."
    echo 'Creating Python virtual environment and activating it...'
    python3 -m venv venv            # Create the virtual enviroment
    source venv/bin/activate        # Activate it

    echo 'Installing dependencies...'
    pip install -r requirements.txt # Install dependencies
    echo "Tasks done: Created Python virtual environment, Installed dependencies"
    echo '-----------------------------------------|  Pieno installed  |-----------------------------------------'
else
    echo "Virtual environment found."
    if [ "$(venv/bin/pip3 freeze)" != "$(cat requirements.txt)" ]; then
        echo "Virtual environment doesn't contain right modules."
        echo 'Installing dependencies...'
        pip install -r requirements.txt # Install dependencies
        echo "Tasks done: Installed dependencies"
        echo '-----------------------------------------|  Pieno installed  |-----------------------------------------'
    else
        echo "All needed modules already installed."
        echo "Tasks done: None"
        echo '-----------------------------------|  Pieno was already installed  |-----------------------------------'
    fi
fi
echo "Staring pieno..."

venv/bin/python3 ./app.py