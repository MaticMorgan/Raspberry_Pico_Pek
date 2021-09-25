from machine import Pin
from utime import sleep


A1 = Pin(15, Pin.OUT) #rumena
A2 = Pin(14, Pin.OUT) #bela
B1 = Pin(13, Pin.OUT) #rdeča
B2 = Pin(12, Pin.OUT) #modra

def K1():
    A1.high()
    A2.low()
    B1.low()
    B2.low()
    
def K2():
    A1.low()
    A2.high()
    B1.low()
    B2.low()
    
def K3():
    A1.low()
    A2.low()
    B1.high()
    B2.low()
    
def K4():
    A1.low()
    A2.low()
    B1.low()
    B2.high()

#spremenljivka za si zapomnit kateri korak se je nazadnje izvršil
korak = K1

# def naprej():
#     if (korak == K1):
#         K4()
#         korak = K4
#     elif (korak == K2):
#         K3()
#         korak = K3
#     elif (korak == K3):
#         K1()
#         korak = K1
#     elif (korak == K4):
#         K2()
#         korak = K2
# 
# def nazaj():
#     if (korak == K1):
#         K3()
#         korak = K3
#     elif (korak == K2):
#         K4()
#         korak = K4
#     elif (korak == K3):
#         K2()
#         korak = K2
#     elif (korak == K4):
#         K1()
#         korak = K1

def naprej():
    A1.high()
    B1.low()
    A2.low()#ta dva damo extra na 0, za situacije, ko na novo prikličemo funkcijo naprej
    B2.low()
    sleep(0.5)
    A1.low()
    A2.low()
    B1.low()
    B2.high()
    sleep(0.5)
    A1.low()
    A2.high()
    B1.low()
    B2.low()
    sleep(0.5)
    A1.low()
    A2.low()
    B1.high()
    B2.low()
    sleep(0.5)

def nazaj():
    A2.high()
    B1.low()
    A1.low()#ta dva damo extra na 0, za situacije, ko na novo prikličemo funkcijo naprej
    B2.low()
    sleep(0.5)
    A2.low()
    B2.high()
    sleep(0.5)
    A1.high()
    B2.low()
    sleep(0.5)
    A1.low()
    B1.high()
    sleep(0.5)
    
while True:
    naprej()
    sleep(1)
#     naprej()
#     sleep(1)
#     nazaj()
#     sleep(1)
#     nazaj()
#     sleep(1)