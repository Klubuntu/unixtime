from os import system as os
import time

while True:
	print(int(round(time.time() * 1000)))
	time.sleep(0.05)
	os('clear')
