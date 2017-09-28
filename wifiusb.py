# https://askubuntu.com/questions/642511/how-to-autorun-files-and-scripts-in-ubuntu-when-inserting-a-usb-stick-like-autor

# or just read a file that's on a USB for the password.

# WIFI_CLI_NAME=cool-wifi pip install wifi

from wifi import Cell, Scheme

cell = Cell.all('wlan0')[0]
scheme = Scheme.for_cell('wlan0', 'home', cell, passkey)
scheme.save()
scheme.activate()
