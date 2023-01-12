import subprocess
import os

if 'nt' in os.name:
    return (subprocess.Popen('dmidecode.exe -s system-uuid'.split()))
else:
    return(subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split()))
