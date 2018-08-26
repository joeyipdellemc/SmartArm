import time
import pigpio 

# GPIO to Servos [12, 16, 20, 21, 19, 13]
SERVOS = [12, 16, 20, 21, 19, 13]

#connect to pigpiod daemon
pi = pigpio.pi()
angle = 2000
pi.set_mode(SERVOS[2], pigpio.OUTPUT)
pi.set_servo_pulsewidth(SERVOS[2], angle)

for i in range( 1,1000,20):
	angle -= 20
	print (angle)
	pi.set_servo_pulsewidth(SERVOS[2], angle)
	time.sleep(0.3)	

#cleanup
#pi.set_mode(SERVOS[2], pigpio.INPUT)
#disconnect
#pi.stop()
