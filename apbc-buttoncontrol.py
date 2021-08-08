import pyfirmata
import time
import screen_brightness_control as sbc

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[8].mode = pyfirmata.INPUT
board.digital[9].mode = pyfirmata.INPUT
board.digital[10].mode = pyfirmata.INPUT
board.digital[11].mode = pyfirmata.INPUT

while True:
    sw1 = board.digital[8].read()
    sw2 = board.digital[9].read()
    sw3 = board.digital[10].read()
    sw4 = board.digital[11].read()
    if sw1 is True:
        sbc.fade_brightness(25)
        print(sbc.get_brightness())
    if sw2 is True:
        sbc.fade_brightness(25)
        print(sbc.get_brightness())        
    if sw3 is True:
        sbc.fade_brightness(25)
        print(sbc.get_brightness())        
    if sw4 is True:
        sbc.fade_brightness(25)
        print(sbc.get_brightness())
