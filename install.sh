#!/bin/bash

venv_path="venv"

echo '---------------------------------------|  Pieno installer 1.2  |---------------------------------------'

if [ ! -d "$(venv_path)" ]; then
    echo "No Python virtual environment in this directory.."
    echo 'Creating Python virtual environment and activating it...'
    python3 -m venv "$(venv_path)"            # Create the virtual enviroment
    source "$(venv_path)"/bin/activate        # Activate it

    echo 'Installing dependencies...'
    pip install -r requirements.txt # Install dependencies
    echo '-----------------------------------------|  Pieno installed  |-----------------------------------------'
else
    echo "Virtual environment found."
    if [ "$("$(venv_path)"/bin/pip3 freeze)" != "$(cat requirements.txt)" ]; then
        echo "Virtual environment doesn't contain right modules."
        if [ "$(read -rsp "Install needed modules? (Y/n)")" == "y" ] || [ "$(read -rsp "Install needed modules? (Y/n)")" == "Y" ] ; then
            echo 'Installing dependencies...'
            pip install -r requirements.txt # Install dependencies
            echo '-----------------------------------------|  Pieno installed  |-----------------------------------------'
        elif [ "$(read -rsp "Install needed modules? (Y/n)")" == "n" ] || [ "$(read -rsp "Install needed modules? (Y/n)")" == "N" ]; then
            echo "To use a different virtual environment, specify the path on the top of the \"install.sh\" file"
            echo "Exiting..."
            echo '--------------------------------|  WARNING Pieno not fully installed  |--------------------------------'
            exit 1
        fi
    else
        echo "All needed modules already installed."
        echo '-------------------------------------|  Pieno was already installed  |-------------------------------------'
    fi
fi

if [ "$(read -rsp "Start Pieno? (Y/n)")" == "y" ] || [ "$(read -rsp "Start Pieno? (Y/n)")" == "Y" ] ; then
        echo 'Installing dependencies...'
        pip install -r requirements.txt # Install dependencies
        echo '-----------------------------------------|  Pieno installed  |-----------------------------------------'
    elif [ "$(read -rsp "Start Pieno? (Y/n)")" == "n" ] || [ "$(read -rsp "Start Pieno? (Y/n)")" == "N" ]; then
        echo "To use a different virtual environment, specify the path on the top of the \"install.sh\" file"
        echo "Exiting..."
        echo '--------------------------------|  WARNING Pieno not fully installed  |--------------------------------'
        exit 1
    fi

exit 0