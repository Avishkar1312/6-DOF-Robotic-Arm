from Adafruit_PCA9685 import PCA9685
from time import sleep

def angle_to_pulse(angle):                     # Used to generate pulses form the desired angle
    pulse = int(375 + (angle / 90.0) * 225)    # Maps 0 to 180 to pulse width (150-600)
    return max(150, min(pulse, 600))           # Bounds the pulse


print("Initializing PCA9685...")
pwm = PCA9685(busnum=1)                        # I2C communication
pwm.set_pwm_freq(60)                           # PWM frequency is set to 60 Hz
print("PCA9685 Initialized. Frequency set to 60Hz.")

channel = 0                                    # Enter the desired channle of the servo driver
desired_angle = 60                             # Enter the deisred angle
current_angle = 0                              # Enter the current angle

step = 2 if desired_angle>= 0 else -5
for angle in range(int(current_angle), int(desired_angle - current_angle) + step, step):
    pwm.set_pwm(channel, 0, angle_to_pulse(angle))
    sleep(0.02)
pwm.set_pwm(channel, 0,0)
current_angle=desired_angle
         
print("Servo moved successfully.")


