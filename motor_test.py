from gpiozero import Motor
from time import sleep

# Define the motors
# Motor(forward_pin, backward_pin, enable_pin)
left_motor = Motor(forward=5, backward=6, enable=12)
right_motor = Motor(forward=22, backward=23, enable=13)

print("Testing Left Motor Forward...")
left_motor.forward(speed=0.5) # 50% speed
sleep(2)
left_motor.stop()

print("Testing Right Motor Forward...")
right_motor.forward(speed=0.5)
sleep(2)
right_motor.stop()

print("Testing Both Backwards...")
left_motor.backward(speed=0.5)
right_motor.backward(speed=0.5)
sleep(2)
left_motor.stop()
right_motor.stop()

print("Test Complete.")
