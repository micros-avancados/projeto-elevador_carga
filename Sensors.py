import RPi.GPIO as IO
import MySQLdb as db
import time
import sys

#Startup configuration
IO.setwarnings(False)
IO.setmode(IO.BCM)

#Input pins
IO.setup(4, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(13, IO.IN)
IO.setup(19, IO.IN)
IO.setup(26, IO.IN)

#Output pins
IO.setup(12, IO.OUT)
IO.setup(16, IO.OUT)
IO.setup(20, IO.OUT)
IO.setup(21, IO.OUT)

print("Starting system...")

#Database configuration/connection
database = db.connect('localhost', 'monitor', 'password', 'packages')
cur = database.cursor()
time.sleep(10)

#Activate outputs
IO.output(12, 1)
IO.output(16, 1)
IO.output(20, 1)
IO.output(21, 1)
x = 0

while 1:
    #Checks if GPIO pins received any signal;
    #shutdown occurs after 10 failed detection attempts
    if(x == 10):
        IO.output(12, 0)

    if(IO.input(4) == False and x == 10):
        IO.output(12, 1)
        time.sleep(5)
        continue
    
    if(IO.input(16) == True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 1)")
            print("Data committed!")
            time.sleep(5)
            continue

    if(IO.input(20) == True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 2)")
            print("Data committed!")
            time.sleep(5)
            continue

    if(IO.input(21) == True):
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
