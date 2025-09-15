from machine import Pin
from utime import sleep
import urandom  # MicroPython random module

sleep(0.01)  # Wait for USB to connect
print("Hello, Pi Pico!")

# Setup LED on GPIO5
led = Pin(5, Pin.OUT)

while True:
    # Generate random temperature between 10 and 20
    temp = 10 + urandom.getrandbits(4) % 11  # 10–20 inclusive
    print("Temperature:", temp, "°C")

    # If temperature > 15 → LED ON, else OFF
    if temp > 15:
        led.value(1)  # Turn LED ON
        print("LED ON (Temp > 15)")
    else:
        led.value(0)  # Turn LED OFF
        print("LED OFF (Temp <= 15)")

    sleep(1)  # Wait 1 second before next reading
