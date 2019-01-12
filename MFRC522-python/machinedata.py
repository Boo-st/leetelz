import RPi.GPIO as GPIO
import MFRC522
import signal
import Read
import dht11

test = Read.machinedata()
test1 = dht11.i()

print(test, test1)