#!/bin/bash

echo '----------------------------------------  Pieno installer 1.0  ----------------------------------------'

pip install -r requirements.txt # Install dependencies

python3 -m venv venv            # Create the virtual enviroment
source venv/bin/activate        # Activate it

echo '----------------------------------------    Pieno installed    ----------------------------------------'
echo
echo 'Starting Pieno...'