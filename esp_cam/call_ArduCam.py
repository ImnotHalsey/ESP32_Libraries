from machine import Pin, SPI
from utime import sleep_ms
from arducam import Camera


# Define pin numbers
SCK_PIN = 18
MISO_PIN = 23
MOSI_PIN = 33
CS_PIN = 32

# Initialize SPI bus
spi = SPI(1, baudrate=2000000, polarity=0, phase=0, sck=Pin(SCK_PIN), miso=Pin(MISO_PIN), mosi=Pin(MOSI_PIN))

# Initialize Chip Select (CS) pin
cs = Pin(CS_PIN, Pin.OUT)

# Create ArduCam Camera object
cam = Camera(spi, cs)

# Onboard LED
onboard_LED = Pin(2, Pin.OUT)

# Set resolution (e.g., 640x480)
cam.set_resolution(cam.RESOLUTION_640X480)

# Capture and save photo
def take_photo():
    onboard_LED.on()
    cam.capture_jpg()
    sleep_ms(200)
    filename = cam.filemanager("image.jpg")
    cam.saveJPG(filename)
    onboard_LED.off()

# Take a photo
take_photo()
