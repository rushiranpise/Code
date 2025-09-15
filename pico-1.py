from machine import Pin
from utime import sleep
import dht

sleep(0.01)  # Wait for USB to connect
print("Hello, Pi Pico!")

# Setup DHT22 sensor on GP15
sensor = dht.DHT22(Pin(15))

# Setup Green LED on GPIO6
green_led = Pin(6, Pin.OUT)

while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C, Humidity:", hum, "%")

        # Green LED logic: ON if temperature > 25, OFF otherwise
        # (You can adjust the threshold if needed)
        if temp > 25:
            green_led.value(1)
            print("Green LED ON (Temp > 25)")
        else:
            green_led.value(0)
            print("Green LED OFF (Temp <= 25)")

    except OSError as e:
        print("Failed to read sensor.")

    sleep(1)  # Wait 1 second before next reading
