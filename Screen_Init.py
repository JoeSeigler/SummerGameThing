from machine import Pin, SPI
from ili9341 import Display, color565
# Create the SPI interface
def initScreen():
    spi = SPI(
        0,
        baudrate=40000000,
        sck=Pin(22),
        mosi=Pin(19)
    )

    # Initialize the display
    display = Display(
        spi,
        cs=Pin(18),
        dc=Pin(21),
        rst=Pin(20)
    )

