from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time
import tree

#inicializacija LCDja in i2c komunikacije za ta LCD
i2c = I2C(id=0,scl=Pin(9),sda=Pin(8),freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)

led = Pin(25, Pin.OUT)

meni = tree.make_tree()
active_node = meni

#to so gumbi za upravljanje LCD menija
up = Pin(16, Pin.IN, Pin.PULL_DOWN)
down = Pin(17, Pin.IN, Pin.PULL_DOWN)
do = Pin(18, Pin.IN, Pin.PULL_DOWN)
undo = Pin(19, Pin.IN, Pin.PULL_DOWN)
#enter = Pin(20, Pin.IN, Pin.PULL_DOWN)

trenutna_vrstica = 0

def prva_vrstica():
    
    lcd.move_to(0,0)
    
    if(active_node.name == 'Main menu'):
        for idx, kid in enumerate(active_node.children):
            if(trenutna_vrstica % 4 == idx):
                is_active = chr(0) + ' '
            else:
                is_active = '  '
            lcd.putstr(is_active + kid.name + "\n")
    else:
        lcd.putstr(active_node.name + "\n")
        for idx, kid in enumerate(active_node.children):
            num_lines = len(active_node.children)
            if((trenutna_vrstica % num_lines) == idx):
                is_active = chr(0) + ' '
            else:
                is_active = '  '
            lcd.putstr(is_active + kid.name + "\n")
        
#definicija za narisat srce
srce = bytearray([0x00,0x0a,0x1f, 0x1f, 0x0e,0x04,0x00,0x00])
lcd.custom_char(0, srce)

#Picopek initialise
lcd.clear()
prva_vrstica()

#Do picopek things
while True:

    lcd.move_to(0,0)
    #Premik po vrstici
    if(up.value() or down.value()):
        if(up.value()):
            trenutna_vrstica -= 1
        elif(down.value()):
            trenutna_vrstica += 1
        prva_vrstica()
        time.sleep(0.2)
    #Izbira ali undo    
    elif(do.value() or undo.value()):
        lcd.clear()
        if(do.value()):
            active_node = active_node.children[trenutna_vrstica]
            print(active_node.children)
            if(active_node.children == []):
                (active_node, path) = active_node.FindRoot()  #zacni od zacetka kazat menu
                print(active_node)
                #print(path[0] + '\n' + path[1] + '\n' + path[2] + '\n')
                led.high()
                lcd.putstr(path[0] + '\n' + path[1] + '\n' + path[2] + '\n')
                time.sleep(10)
                #vstavi funkcijo za pečenje
                
                lcd.clear()
                prva_vrstica()
                led.low()
                #spremeni en bool, da bo na koncu while True nardilo nekaj drugega, npr. resetiralo menu
            #else:
                
        elif(undo.value()):
            if(active_node.parent != None):
                active_node = active_node.parent
            else:
                led.high()
                #opozori uporabnika, da je stisnu nekaj, kar ne počne nič
        trenutna_vrstica = 0
        prva_vrstica()
        time.sleep(0.2)
