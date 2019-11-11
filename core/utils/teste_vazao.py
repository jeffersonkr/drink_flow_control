import RPi.GPIO as GPIO
import time
import sys

FLOW_SENSOR = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def count_pulse(channel):
    start = time.time()
    global count
    count = count+1
    end = time.time()-start
    print(count, end)


GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=count_pulse)
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()