#!/bin/bash

echo '----------------------------------------  Pieno installer 1.0  ----------------------------------------'

python3 -m venv venv            # Create the virtual enviroment
source venv/bin/activate        # Activate it

pip install -r requirements.txt # Install dependencies

echo '----------------------------------------    Pieno installed    ----------------------------------------'
echo
echo 'Starting Pieno...'
venv/bin/python3