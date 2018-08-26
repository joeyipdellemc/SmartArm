import time
import pigpio 

# GPIO to Servos [12, 16, 20, 21, 19, 13]
SERVOS = [12, 16, 20, 21, 19, 13]

#connect to pigpiod daemon
pi = pigpio.pi()
 
# setup pin as an output
for PIN in SERVOS:
	pi.set_mode(PIN, pigpio.OUTPUT)
	
	pi.set_servo_pulsewidth(PIN, 1000)
	time.sleep(0.1)
	
	pi.set_servo_pulsewidth(PIN, 2000)
	time.sleep(0.1)
	
	pi.set_servo_pulsewidth(PIN, 1500)
	time.sleep(0.5)

#cleanup
pi.set_mode(PIN, pigpio.INPUT)
#disconnect
pi.stop()
