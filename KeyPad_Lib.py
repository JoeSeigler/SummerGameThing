from machine import Pin

r1 = Pin(2, Pin.OUT)
r2 = Pin(3, Pin.OUT)
r3 = Pin(4, Pin.OUT)
c1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
c2 = Pin(7, Pin.IN, Pin.PULL_DOWN)
c3 = Pin(8, Pin.IN, Pin.PULL_DOWN)

def detectPress():
    wiresOn()
    if(c1.value() == 1 or c2.value() == 1 or c3.value() == 1):
        return 1
def wiresOn():  
    r1.on()
    r2.on()
    r3.on()
def wiresOff():
    r1.off()
    r2.off()
    r3.off()
def detectWhichKey():
    wiresOff()
    r1.on()
    if(c1.value() == 1):
        return 1
    if(c2.value() == 1):
        return 2
    if(c3.value() == 1):
        return 3
    r1.off()
    r2.on()
    if(c1.value() == 1):
        return 4
    if(c2.value() == 1):
        return 5
    if(c3.value() == 1):
        return 6
    r2.off()
    r3.on()
    if(c1.value() == 1):
        return 7
    if(c2.value() == 1):
        return 8
    if(c3.value() == 1):
        return 9
    r3.off()
    return 0
    

