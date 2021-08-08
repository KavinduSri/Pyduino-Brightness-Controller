print('''
███████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░█████████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
███████████████████████████████████████████████████████████████
                                              -Kavindu Sri-''')
import pyfirmata
import os
import time
import screen_brightness_control as sbc

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[9].mode = pyfirmata.INPUT
def anim() :                   
    os.system('cls')

    print("\nProccessing.../ ")
    time.sleep(0.1)


    print("\nProccessing...- ")
    time.sleep(0.1)
    os.system('cls')

    print("\nProccessing...\ ")
    time.sleep(0.1)
    os.system('cls')

    print("\nProccessing...| ")
    time.sleep(0.1)
    os.system('cls')

    print("\nProccessing.../ ")
    time.sleep(0.1)


    print("\nProccessing...- ")
    time.sleep(0.1)
    os.system('cls')

    print("\nProccessing...\ ")
    time.sleep(0.1)
    os.system('cls')

    print("\nProccessing...| ")
    time.sleep(0.1)
    os.system('cls')

def anim2() :

    print("Proccess complete...")

while True:
    
    sw1 = board.digital[9].read()
    if sw1 is True:

        print("Button Input is Successfull...")
        time.sleep(2)
        anim()
        print('Before Brightness : ',sbc.get_brightness())
        i = int(input('Enter Want bright: '))
        anim()
        anim2()
        sbc.fade_brightness(i)
        print('Now Brightness is: ',sbc.get_brightness())
