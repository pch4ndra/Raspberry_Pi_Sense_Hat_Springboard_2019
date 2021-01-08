#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()
curr = 0

try:
	while True:
		temp = sense.get_temperature()
		temp = 1.8 * round(temp, 1) + 32
		if (temp >= 90):
			sense.show_message("T: " + str(temp), back_colour=[255,0,0])
		else:
			sense.show_message("T: " + str(temp), back_colour=[0,0,255])

		if abs(curr-temp) > 0.5:
			curr = temp
			print("Temperature F", temp)
			humidity = sense.get_humidity()
			humidity = round(humidity, 1)
			print("Humidity: ", humidity)
			pressure = sense.get_pressure()
			pressure = round(pressure, 1)
			print("Pressure: ", pressure)
			print("---------------------------------")
			sense.show_message("H: " + str(humidity) + " P: " + str(pressure), scroll_speed=(0.08))
		else:
			print("Change was less than 0.5")
		time.sleep(2)
		sense.clear()
except KeyboardInterrupt:
	pass

sense.clear()
