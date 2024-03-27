
## PI Setup

- sudo raspi-config
- sudo apt install python3-pip
- enable spi
- [Neopixels](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)
  - sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
  - sudo python3 -m pip install --force-reinstall adafruit-blinka
- [Numpy](https://stackoverflow.com/questions/53784520/numpy-import-error-python3-on-raspberry-pi)
  - sudo apt-get install libatlas-base-dev

## Raspi Notes
- [Headles Pi Zero Set up](https://desertbot.io/blog/ssh-into-pi-zero-over-usb)
- raspi-config
- default user, pass: pi, raspberry
- Login: ssh pi@(IP or raspberrypi). Username: pi, Pass: greyman
- VNC pass: greyman69
- sudo su
- source virtual_env/bin/activate
- python x.py

sudo nano /etc/dhcpcd.conf
interface eth0
static ip_address=<desired IP address>/24

## GEDIT
Press Ctrl+O to save the file, and then press Ctrl+X to exit the text editor.
- linux - use gedit for text editing (sudo gedit file)

## Screens
Screens: Run screen that stays on so you don't have to be constantly connected

- Run screen: screen bash
- Show screens: screen -list
- Connect to screen: screen -r (name if multiple)
- End Screen: CTRL+A then D
- Kill Screen: CTRL D

## Pi-Plates
- RPi.GPIO
- spidev
- six

## Trouble shooting

sudo service networking restart
- ssh key issues: ssh-keygen -R "your server hostname or IP"
[Raspberry PI numpy](https://stackoverflow.com/questions/53784520/numpy-import-error-python3-on-raspberry-pi)
- sudo apt-get install libatlas-base-dev

### Wiki Notes

- pip install rpi.gpio


