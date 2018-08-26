import time
import pigpio 
PIN = 12
 
#connect to pigpiod daemon
pi = pigpio.pi()
 
# setup pin as an output
pi.set_mode(PIN, pigpio.OUTPUT)
 
pi.set_servo_pulsewidth(PIN, 500)
time.sleep(1)
pi.set_servo_pulsewidth(PIN, 2500)
time.sleep(1)
 
#cleanup
pi.set_mode(PIN, pigpio.INPUT)
#disconnect
pi.stop()
