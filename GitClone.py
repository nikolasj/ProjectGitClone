#!/usr/bin/env python
# Script to clone all the github repos that a user is watching

import subprocess


def main():
    print("Start!")
    print("----------------------------------")
    subprocess.call('cd /home/nicolas/test_git/Lab_C/;echo "one" | git pull —no-edit https://github.com/nikolasj/Lab_C.git feature', shell=True)
    subprocess.call('cd /home/nicolas/test_git/Lab_C/;echo "one" | touch Changes.txt', shell=True)
    subprocess.call('cd /home/nicolas/test_git/Lab_C/;echo "one" | git checkout feature', shell=True)
    subprocess.call('cd /home/nicolas/test_git/Lab_C/;echo "one" | git diff feature^ >> Changes.txt', shell=True)
    print("----------------------------------")
    print("Finish!")

if __name__ == "__main__" :
    main()
