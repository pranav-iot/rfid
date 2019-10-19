from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
	text=input("Enter new data on card:")
	print("Now place the card!")
	reader.write(text)
	print("Data successfully written!")
	sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise