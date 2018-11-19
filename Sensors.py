import RPi.GPIO as IO
import MySQLdb as db
import time
import sys

#Startup and configuration pins
IO.setwarnings(False)
IO.setmode(IO.BCM)

#Input pins
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)
IO.setup(19,IO.IN)
IO.setup(26,IO.IN)

#Output pins
IO.setup(12,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(21,IO.OUT)

print("Starting system...")

#Database configuration/connection
database = db.connect('localhost', 'monitor', 'password', 'packages')
cur = database.cursor()

time.sleep(10)

x = 0
while 1:
    #Checks if GPIO pins received any signal
    #Shutdown occurs after 10 failed detection attempts
    if(IO.input(6)==True and x == 10):
        #set pin 12 high
        time.sleep(5)
        continue
    if(IO.input(13)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 1)")
            print("Data committed!")
            time.sleep(5)
            continue
    if(IO.input(19)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 2)")
            print("Data committed!")
            time.sleep(5)
            continue
    if(IO.input(26)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 3)")
            print("Data committed!")
            time.sleep(5)
            continue
    else:
        print("Nothing detected on sensors!")
        x = x + 1
        time.sleep(5)
        continue

#Close database connection
print("Closing database...")
database.close()
time.sleep(5)
print("Shutting down system...")
time.sleep(5)
sys.exit()
