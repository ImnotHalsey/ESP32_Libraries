import utime
import ntptime

def get_timestamp():
    timezone_offset = 5 * 60 * 60 + 30 * 60
    try: ntptime.settime()
    except ImportError: pass  
    current_time = utime.time()
    ist_time = current_time + timezone_offset
    formatted_time = utime.localtime(ist_time)
    timestamp = "{:04}{:02}{:02}{:02}{:02}{:02}".format(*formatted_time[:6])
    return str(timestamp)

