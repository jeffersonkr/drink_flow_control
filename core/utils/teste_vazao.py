import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime

count = 0
FLOW_SENSOR = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def count_pulse(channel):
    # Called if sensor output changes
    timestamp = time.time()
    stamp = datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    if GPIO.input(channel):
        # No magnet
        print("Sensor HIGH " + stamp)
    else:
        # Magnet
        print("Sensor LOW " + stamp)


GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=count_pulse, bouncetime=200)
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