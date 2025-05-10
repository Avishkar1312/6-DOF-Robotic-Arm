from Adafruit_PCA9685 import PCA9685
from time import sleep

def angle_to_pulse(angle):                   # Used to generate pulses form the desired angle
    pulse = int(375 + (angle / 90.0) * 225)  # Maps 0 to 180 to pulse width (150-600)
    return max(150, min(pulse, 600))         # Bounds the pulse

# Initialize PCA9685
print("Initializing PCA9685...")
pwm = PCA9685(busnum=1)
pwm.set_pwm_freq(60)  # Set PWM frequency to 60Hz
print("PCA9685 Initialized. Frequency set to 60Hz.")

# Assign your desired angle
desired_angle = 80

# Convert the desired angle to the corresponding pulse width
pulse = angle_to_pulse(desired_angle)

# Set the servo to the desired angle
pwm.set_pwm(1, 0, pulse)   #1 over here refers to the channel on the servo driver and can be set to custom channle as well

print(f"Servo moved to {desired_angle} degrees and stopped.")
