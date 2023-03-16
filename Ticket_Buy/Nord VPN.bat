@echo off
C:
cd "C:\Program Files\NordVPN\"

:x

nordvpn -c -g "United States"
timeout 500

nordvpn -c -g "Canada"
timeout 500

nordvpn -c -g "United Kingdom"
timeout 500

goto x