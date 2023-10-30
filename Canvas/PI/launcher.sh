#!/bin/sh
# launcher.sh
# navigate to directory, activate venv, run

# vars
VENV_NAME="v_env/bin/activate"
SCRIPT="clock.py"
WDIR="/home/pi/cottage"

cd $WDIR
. $VENV_NAME
sudo python3 $SCRIPT

deactivate
