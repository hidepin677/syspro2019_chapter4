import time
import RPi.GPIO as GPIO
def setservo(deg):
   servo.ChangeDutyCycle(2.5 + 9.5 * ( deg + 90) / 180 )

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

for i in range(5):
	servo.ChangeDutyCycle(bottom)
        setservo(-90)
	time.sleep(1.0)

	servo.ChangeDutyCycle(middle)
        setservo(0)
	time.sleep(1.0)

	servo.ChangeDutyCycle(top)
        setservo(90)
	time.sleep(1.0)




