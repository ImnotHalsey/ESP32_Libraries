from time import sleep 
import camera, machine,uos
from utilities import get_timestamp


led = machine.Pin(4, machine.Pin.OUT)

def take_photo(flash=None):
    try:
        try: 
            camera.init(0, format=camera.JPEG)
            if flash:led.on()
            img = camera.capture()
            if flash:led.off()
            try:
                file_path = f"SD/{get_timestamp()}.jpg"
                with open(file_path, "wb") as file:
                    file.write(bytearray(img))
                print(f"Photo saved : {file_path}")
                return True, file_path
            except Exception as e:
                print(f"Error saving photo: {e}")
                return False, None
        except Exception as e:
            print(f"Error Initiating Camera: {e}")
            return False, None
    finally:
        camera.deinit()
