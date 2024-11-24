import adafruit_dht
import board
import time

# Use GPIO 17 for the DHT sensor
sensor = adafruit_dht.DHT11(board.D17)  # Change to DHT22 if you're using that

try:
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            print(f"Temperature: {temperature:.1f}°C")
            print(f"Humidity: {humidity:.1f}%")
        except RuntimeError as error:
            # Handle occasional sensor read errors
            print(f"Error: {error.args[0]}")
        time.sleep(2)  # Wait 2 seconds before reading again
except KeyboardInterrupt:
    print("Exiting...")
finally:
    sensor.exit()
