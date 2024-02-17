#!/bin/sh
# launcher.sh
# navigate to directory, activate venv, run

# Add this line at the beginning of your shell script
sudo exec >> /home/pi/cottage/myscript.log 2>&1


# vars
VENV_NAME="v_env/bin/activate"
SCRIPT="CC.py"
WDIR="/home/pi/cottage"

cd $WDIR
. $VENV_NAME
sudo python3 $SCRIPT

deactivate
