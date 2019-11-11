import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime

count = 0
start = datetime.now()
count_per_sec = 0
FLOW_SENSOR = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def count_pulse(channel):
    global count, start, count_per_sec
    count = count+1
    if datetime.now() - start == 1:
        count_per_sec += count
        print(count_per_sec)


GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=count_pulse)
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        end = datetime.now()
        print('\ncaught keyboard interrupt!, bye')
        total_time = end - start
        frequency = count/total_time
        GPIO.cleanup()
        sys.exit()