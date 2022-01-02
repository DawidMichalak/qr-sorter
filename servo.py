import RPi.GPIO as GPIO
import time
import numpy

#Servo(19, True)
#Servo(26, False)
class Servo:    
    def __init__(self, servoPin, flip=False):
        self.servoPin = servoPin
        self.openPosition = 90
        self.closePosition = 0
        self.rezolution = 50
   
        if flip:
            self.openPosition = 0
            self.closePosition = 90
        
        self.position = self.openPosition
        self.open() 
        
    def close(self):
        self.move(self.closePosition)
        
    def open(self):
        self.move(self.openPosition)
        
    def move(self, newPosition):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPin, GPIO.OUT)
        
        pwm = GPIO.PWM(self.servoPin, self.rezolution)   
        pwm.start(self.position)
        angle = numpy.linspace(self.position, newPosition, self.rezolution)
        
        for a in angle:
            duty = a / 18 + 2
            pwm.ChangeDutyCycle(duty)
            time.sleep(1/self.rezolution)
            
        self.position = newPosition
        pwm.stop(newPosition)