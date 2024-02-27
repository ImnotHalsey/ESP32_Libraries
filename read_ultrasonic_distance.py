from machine import Pin
import time

trigger_pin = Pin(12, Pin.OUT)
echo_pin = Pin(14, Pin.IN)

def read_distance():
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration * 34300) / 2 / 1000000  # Convert to meters
    if distance > 0 and distance < 50:return distance
    else: return None
    
while True:
    dist = read_distance()
    if dist:
        print(f"Distance: {int(dist)} Cms")
        time.sleep(0.25)
