import RPi.GPIO as GPIO
import time

ledpin = 12				# PWM pin connected to LED
servo_pin = 12
servo_freq = 50
# GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(servo_pin,GPIO.OUT)
pi_pwm = GPIO.PWM(servo_pin,servo_freq)		#create PWM instance with frequency
pi_pwm.start(50)				#start PWM of required Duty Cycle 
# while True:
#     for duty in range(0,101,1):
#         pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#         sleep(0.01)


# set pins

# pi = pigpio.pi()

# pi.set_mode(servo_pin, pigpio.OUTPUT)
# pi.set_PWM_frequency(servo_pin, 0)



def send_servo_angle(theta):
    # duty = (theta/180) * 100 * (1/10) + 10
    duty = int(theta/10 + 10)
    # print(duty)
    pi_pwm.ChangeDutyCycle(duty)
    # pi.set_PWM_frequency(servo_pin, freq)

for a in range(0,100):
    send_servo_angle(a)
    time.sleep(.05)

