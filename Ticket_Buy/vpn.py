import os
import time

os.chdir(r'C:\Program Files\NordVPN')

while True:
    os.system('nordvpn -c -g "United States"')
    time.sleep(500)
    os.system('nordvpn -c -g "Canada"')
    time.sleep(500)
    os.system('nordvpn -c -g "United Kingdom"')
    time.sleep(500)