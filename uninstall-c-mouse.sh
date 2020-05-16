#!/bin/bash
echo "Removing opencv"
sudo pip3 uninstall opencv-python
echo "Removing Pyautogui"
sudo pip3 uninstall pyautogui
sudo rm -rf /usr/bin/c-mouse
sudo rm -rf /usr/bin/uninstall-c-mouse
sudo rm -rf /opt/c-mouse
