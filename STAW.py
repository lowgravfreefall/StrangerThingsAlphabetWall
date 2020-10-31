import time
import sys
import board
import neopixel
import os

pixel_pin = board.D18
num_pixels = 50
ORDER = neopixel.GRB
counter = 0
blink_count = 0
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
    )
list = []

alphabet_positions = {'a':43, 'b':42, 'c':41, 'd':40, 'e':39, 'f':38, 'g':37, 'h':36,
                       'i':22, 'j':23, 'k':24, 'l':25, 'm':26, 'n':27, 'o':28, 'p':29, 'q':30,
                       'r': 15, 's':14, 't':13, 'u':12, 'v':11, 'w': 10, 'x':9, 'y': 8, 'z':7}

def main():
    login()
    
def login():
    print("************ LOGIN **************")
    username="mbrenner"
    password="admin"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
        time.sleep(2)
        os.system('clear')
        menu()

def menu():
    print("""
        ___  _       _           _          _     _    _       _ _ 
       / _ \| |     | |         | |        | |   | |  | |     | | |
      / /_\ \ |_ __ | |__   __ _| |__   ___| |_  | |  | | __ _| | |
      |  _  | | '_ \| '_ \ / _` | '_ \ / _ \ __| | |/\| |/ _` | | |
      | | | | | |_) | | | | (_| | |_) |  __/ |_  \  /\  / (_| | | |
      \_| |_/_| .__/|_| |_|\__,_|_.__/ \___|\__|  \/  \/ \__,_|_|_|
              | |                                                  
              |_|                                                                                                                                                           
            """)
    print()

    choice = input("""
                      1: RUN
                      2: Happy Halloween
                      3: Talk to Joyce
                      4: Blink Lights
                      5: Quit/Log Out

                      Please enter your choice: """)
    if choice == "1":
         run()
    elif choice == "2":
        happy_halloween()
    elif choice == "3":
        talk_joyce()
    elif choice == "4":
        blink()
    elif choice=="5":
        sys.exit
    else:
        print("You must only select either 1,2,3,4, or 5.")
        print("Please try again")
        menu()

def run():
    list.append("run")
    for item in list:
        for character in item:
            if character in alphabet_positions:
                pixels[alphabet_positions[character]] = (255, 255, 255)
                pixels.show()
                time.sleep(1)
                pixels[alphabet_positions[character]] = (0, 0, 0)
                pixels.show()
                time.sleep(1)
    list.clear()
    flash()
    os.system('clear')
    menu()
def happy_halloween():
    list.append("happy halloween")
    for item in list:
        for character in item:
            if character in alphabet_positions:
                pixels[alphabet_positions[character]] = (255, 255, 255)
                pixels.show()
                time.sleep(.6)
                pixels[alphabet_positions[character]] = (0, 0, 0)
                pixels.show()
                time.sleep(.6)
    list.clear()
    os.system('clear')
    flash()
    menu()
    
def talk_joyce():
    textField = input("Talk to Joyce: ").lower()

    for item in textField.replace(" ", ""):
        list.append(str(item))

    for item in list:
        for character in item:
            if character in alphabet_positions:
                pixels[alphabet_positions[character]] = (255, 255, 255)
                pixels.show()
                time.sleep(.7)
                pixels[alphabet_positions[character]] = (0, 0, 0)
                pixels.show()
                time.sleep(.7)
    list.clear()
    flash()
    os.system('clear')
    clearC()
    menu()
    
def flash():
    global counter
    while counter < 3:
        rainbow_cycle(0.001)
        counter += 1
    
    pixels.fill((0, 0, 0))
    pixels.show()
    clearC()

def clearC():
    global counter
    counter = 0
    
def blink():
    global counter
    while counter < 4:
        rainbow_cycle(0.001) 
        counter +=1
    pixels.fill((0, 0, 0))
    pixels.show()
    os.system('clear')
    clearC()
    menu()    

#From https://learn.adafruit.com/neopixels-on-raspberry-pi
def wheel(pos):
  
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

main()
