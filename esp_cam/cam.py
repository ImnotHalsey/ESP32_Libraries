from time import sleep 
import urandom, machine, camera
from utilities import get_timestamp


led = machine.Pin(4, machine.Pin.OUT)

def take_photo(flash=None):
    try:
        camera.init(0, format=camera.JPEG)
        if flash: led.on()
        img = camera.capture()
        if flash: led.off()
        camera.deinit()
        file_path = f"photo/{get_timestamp()}"
        with open(file_path, "wb") as file:
            file.write(img)
        print(f"Photo saved: {file_path}")
        return True, file_path
    except Exception as e:
        print(f"Error capturing or saving photo: {e}")
        return 0,0
