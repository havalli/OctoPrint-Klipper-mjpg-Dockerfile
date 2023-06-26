#!/usr/bin/env python

import subprocess
import time
import os
import pwd

OCTOPRINT = ["/opt/octoprint/venv/bin/octoprint", "serve"]

def main():
    # Start klipper
    klipper = subprocess.Popen(['sudo', '-u', 'octoprint', '/runklipper.py'])

    os.setgid(
        1000
    )  # Drop privileges, https://stackoverflow.com/questions/2699907/dropping-root-permissions-in-python#2699996
    os.setuid(1000)
    os.environ['HOME'] = '/home/octoprint'
    # subprocess.Popen('env', shell=True).wait()
    while 1:
        Poctoprint = subprocess.Popen(OCTOPRINT)
        Poctoprint.wait()
        time.sleep(1)


if __name__ == '__main__':
    main()

