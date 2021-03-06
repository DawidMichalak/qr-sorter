import time
import RPi.GPIO as GPIO

pins = [4, 17, 27, 22]

halfStepSequence = [
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW,  GPIO.LOW),
    (GPIO.HIGH, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH, GPIO.HIGH,  GPIO.LOW),
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH,  GPIO.LOW),
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH, GPIO.HIGH),
    ( GPIO.LOW,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH),
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH)]

torqueSequence = [
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH, GPIO.HIGH),
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH),
    (GPIO.HIGH, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH, GPIO.HIGH,  GPIO.LOW)]

class Stepper():
    sequence = []

    def __init__(self, seq):
        GPIO.setup(pins, GPIO.OUT)
        self.sequence = seq

    def moveAsync(self, delay, lock):
        while True:
            with lock:
                for i in range(0, len(self.sequence)):
                    GPIO.output(pins, self.sequence[i])
                    time.sleep(delay)
            GPIO.output(pins, GPIO.LOW)
    
    def move(self, delay, steps, backward=False):
        for i in range(0, steps):
            if backward:
                GPIO.output(pins, self.sequence[(- i % len(self.sequence))])
            else:
                GPIO.output(pins, self.sequence[i % len(self.sequence)])
            time.sleep(delay)
        GPIO.output(pins, GPIO.LOW)
