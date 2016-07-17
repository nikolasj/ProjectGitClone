#!/usr/bin/env python
# Script to clone all the github repos that a user is watching

import subprocess

# test message

def main():
    print("Start!")
    print("----------------------------------")
    subprocess.call('cd /home/cm/test_git/Lab_C/;echo "one" | git pull —no-edit https://github.com/nikolasj/Lab_C.git 1.0-pm', shell=True)
    subprocess.call('cd /home/cm/test_git/Lab_C/;echo "one" | git branch 1.0-pm', shell=True)
    subprocess.call('cd /home/cm/test_git/Lab_C/;echo "one" | git diff 1.0-pm^', shell=True)
    print("----------------------------------")
    print("Finish!")

if __name__ == "__main__" :
    main()