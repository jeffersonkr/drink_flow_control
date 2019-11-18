import json
import time
from datetime import datetime
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
  
class FlowMeter():
    ''' Class representing the flow meter sensor which handles input pulses
        and calculates current flow rate (L/min) measurement
    '''
    
    def __init__(self):
        self.flow_rate = 0.0
        self.last_time = datetime.now()
  
    def _pulse_callback(self, p):
        ''' Callback that is executed with each pulse 
            received from the sensor 
        '''
       
        # Calculate the time difference since last pulse recieved
        current_time = datetime.now()
        diff = (current_time - self.last_time).total_seconds()
       
        # Calculate current flow rate
        hertz = 1 / diff
        self.flow_rate = hertz / 8
       
        # Reset time of last pulse
        self.last_time = current_time
    
    def _get_flowRate(self):
        ''' Return the current flow rate measurement. 
            If a pulse has not been received in more than one second, 
            assume that flow has stopped and set flow rate to 0.0
        '''
       
        if (datetime.now() - self.last_time).total_seconds() > 1:
            self.flow_rate = 0.0
        
        return self.flow_rate
  
    def start_flow_control(self):
        ''' Main function for repeatedly collecting flow rate measurements
            and sending them to the SORACOM API
        '''

        # Configure GPIO pins
        INPUT_PIN = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Init FlowMeter instance and pulse callback
        GPIO.add_event_detect(INPUT_PIN,
                            GPIO.RISING,
                            callback=self._pulse_callback,
                            bouncetime=10)

        # Begin infinite loop
        while True:
            # Get current timestamp and flow meter reading
            timestamp = str(datetime.now())
            flow_rate = self._get_flowRate()
            publish.single("monitoring/", flow_rate, hostname="localhost", port=1883)

            # Delay
            time.sleep(0.1)

if __name__ == "__main__":
    flow_meter = FlowMeter()
    flow_meter.start_flow_control()