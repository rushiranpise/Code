from machine import Pin
from utime import sleep
import urandom  # MicroPython random module

sleep(0.01)  # Wait for USB to connect
print("Hello, Pi Pico!")

# Setup Green LED on GPIO6 (change if needed)
green_led = Pin(6, Pin.OUT)

while True:
    # Generate random pressure between 40 and 50 psi
    pressure = 40 + urandom.getrandbits(4) % 11  # 40–50 inclusive
    print("Pressure:", pressure, "psi")

    # Conditional statement for green LED
    if pressure > 45:
        green_led.value(1)  # Turn Green LED ON
        print("Green LED ON (Pressure > 45 psi)")
    else:
        green_led.value(0)  # Turn Green LED OFF
        print("Green LED OFF (Pressure <= 45 psi)")

    sleep(1)  # Wait 1 second before next reading
