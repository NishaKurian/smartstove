import RPi.GPIO as GPIO
import time
import telegram

	control_a=11
	control_b=13
	ignition=7
	flame=10
	leak=12
	lighth=36
	lightm=38

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(control_a, GPIO.OUT)
GPIO.setup(control_b, GPIO.OUT)
GPIO.setup(ignition, GPIO.OUT)
GPIO.setup(lighth,GPIO.OUT)
GPIO.setup(lightm,GPIO.OUT)
GPIO.setup(flame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leak, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	true=True
	start_time=time.time()
	def flamecontrol(status):
if status=='ON' or status=='MID':


	GPIO.output(control_a,0)
	GPIO.output(control_b,1)
	GPIO.output(ignition,1)

	if flame=='H':
		GPIO.output(lighth,1)
		GPIO.output(lightm,0)
		time.sleep(2)
		print 'stove on-high'
	elif flame=='M':
		GPIO.output(lightm,1)
		GPIO.output(lighth,1)
		time.sleep(3)
		print 'stove on-medium'

		GPIO.output(control_a,0)
		GPIO.output(control_b,0)
		GPIO.output(ignition,0)
		time.sleep(.5)
		data=''