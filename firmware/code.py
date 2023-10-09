import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import board
import digitalio

kbd = Keyboard(usb_hid.devices)

D1 = digitalio.DigitalInOut(board.D1)
D1.direction = digitalio.Direction.OUTPUT

D2 = digitalio.DigitalInOut(board.D2)
D2.direction = digitalio.Direction.OUTPUT

D3 = digitalio.DigitalInOut(board.D3)
D3.direction = digitalio.Direction.OUTPUT

D4 = digitalio.DigitalInOut(board.D4)
D4.switch_to_input(pull=digitalio.Pull.DOWN)

D5 = digitalio.DigitalInOut(board.D5)
D5.switch_to_input(pull=digitalio.Pull.DOWN)

inputs = (D4,D5)
outputs = (D1,D2,D3)
old = [[False,False,False],[False,False,False]]

#使用可能なキーは https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode を参照
keys = [[Keycode.ESCAPE,Keycode.UP_ARROW,Keycode.DELETE],[Keycode.LEFT_ARROW,Keycode.DOWN_ARROW,Keycode.RIGHT_ARROW]]

while True:
    for i in outputs:
        i.value = True
        for j in inputs:
            row = outputs.index(i)
            col = inputs.index(j)
            
            if j.value == True:
                if j.value != old[col][row]:
                    kbd.press(keys[col][row])
                    
            if j.value == False:
                if j.value != old[col][row]:
                    kbd.release(keys[col][row])
            old[col][row] = j.value
        i.value = False
        time.sleep(0.001)