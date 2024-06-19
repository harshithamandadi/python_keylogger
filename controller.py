#learning pynput package in python

#from pynput.mouse import Controller, Button
from pynput.keyboard import Controller

def control_mouse():
    mouse = Controller()
    mouse.position = (0,0)
    mouse.position = (200,400)
    mouse.press(Button.right)
    mouse.release(Button.right)

def control_keyboard():
    text = input("enter the text to be typed\n")
    keyboard = Controller()
    keyboard.type(text)


if __name__ == '__main__':
    #control_mouse()
    control_keyboard()

