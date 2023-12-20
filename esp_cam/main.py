from cam import take_photo
import uos, machine, gc, utime
from send_server import upload_photo
from wifimanager import Call_Manager

wifimanager = Call_Manager()
i = 0

if wifimanager:
    print("Connected to WiFi...")
    uos.mount(machine.SDCard(), "/SD")
    while 1:
        status, path = take_photo(flash=1)
        if status:
            print(i)
            upload_photo(path)
            i = i + 1
            gc.collect()
        else:
            print("Bad Error")
            gc.collect()
else:
    print("Error while connecting to WiFi")