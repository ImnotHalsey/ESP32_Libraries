from wifi_manager import Call_Manager
from cam import take_photo
from time import sleep
import machine, uos


wifimanager = Call_Manager()
def controller():
    i = 0
    if wifimanager:
        print("WiFi Connected")
        while True:
            take_photo(i, flash=1)
            i = i + 1
            sleep(3)
    else:
        print("Unable to connect to WiFi")
                
    
controller()