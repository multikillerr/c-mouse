import pyautogui
def get_resolution():
    file1=open("/opt/c-mouse/width.txt","w")
    file2=open("/opt/c-mouse/height.txt","w")
    width,height=pyautogui.size()
    file1.write(str(width))
    file2.write(str(height))
