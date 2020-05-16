#!/bin/bash
mkdir /opt/c-mouse
sudo mv Project_final.py /opt/c-mouse/
sudo mv get_resolution/ /opt/c-mouse/
sudo mv uninstall-c-mouse.sh /opt/c-mouse/
sudo mv requirements.txt /opt/c-mouse/
sudo mv runner.sh /opt/c-mouse/
sudo mv uninstall-c-mouse.sh /opt/c-mouse/
sudo apt-get install python3
sudo apt-get install cython3
sudo pip3 install -r /opt/c-mouse/requirements.txt
sudo touch /usr/bin/c-mouse 
sudo ln -sf /opt/c-mouse/runner.sh /usr/bin/c-mouse
sudo touch /usr/bin/uninstall-c-mouse
sudo ln -sf /opt/c-mouse/uninstall-c-mouse.sh /usr/bin/uninstall-c-mouse
sudo cython3 --embed /opt/c-mouse/Project_final.py -o /opt/c-mouse/c-mouse.c
sudo gcc -Os -I /usr/include/python3.8 -o /opt/c-mouse/c-mouse /opt/c-mouse/c-mouse.c -lpython3.8 -lpthread -lm -lutil -ldl
sudo chmod +x /opt/c-mouse/runner.sh
sudo chmod +x /opt/c-mouse/uninstall-c-mouse.sh
sudo chmod +x /opt/c-mouse/c-mouse
sudo rm /opt/c-mouse/Project_final.py
sudo rm /opt/c-mouse/requirements.txt
sudo rm /opt/c-mouse/c-mouse.c
sudo rm -rf $PWD
echo "To run type c-mouse on the terminal.."
echo "To uninstall type uninstall-c-mouse"
