from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #Pauses script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def main():
    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(180,400,600,400))

        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r,g,b = pic.getpixel((x,y))

                if b == 195:
                    click(x+180, y+400)
                    time.sleep(0.08)
                    break

if __name__ == '__main__':
    main()
