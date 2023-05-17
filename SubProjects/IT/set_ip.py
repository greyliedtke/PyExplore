import subprocess
subprocess.call("netsh interface ip set address ....".split())

# netsh interface ip set address Local Area Connection static 192.168.0.100 255.255.255.0
# ehternet connection options
# default dns: 8.8.8.8