import RPi.GPIO as IO
import MySQLdb as db
import time
import sys

#Startup configuration
IO.setwarnings(False)
IO.setmode(IO.BCM)

#Input pins
IO.setup(4, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(16, IO.IN)
IO.setup(20, IO.IN)
IO.setup(21, IO.IN)

#Output pins
IO.setup(2, IO.OUT)
IO.setup(14, IO.OUT)
IO.setup(15, IO.OUT)
IO.setup(18, IO.OUT)

print("Starting system...")

#Database configuration/connection
database = db.connect('localhost', 'monitor', 'password', 'packages')
cur = database.cursor()
time.sleep(10)

#Activate outputs
IO.output(2, 1)
IO.output(14, 1)
IO.output(15, 1)
IO.output(18, 1)
x = 0

#System halt
def interrupt():
    while 1:
        if(IO.input(4) == False and x == 10):
            IO.output(2, 1)
            break
        time.sleep(1)

while 1:
    #Checks if GPIO pins received any signal;
    #shutdown occurs after 10 failed detection attempts
    
    if(x == 10):
        IO.output(2, 0)
        interrupt() 
    
    IO.output(14, 0)
    IO.output(14, 1)
    if(IO.input(16) == True):
        with database:
            cur.execute("INSERT INTO test VALUES(default, NOW(), 1)")
            print("Data committed!")
            time.sleep(5)
            continue

    IO.output(15, 0)
    IO.output(15, 1)
    if(IO.input(20) == True):
        with database:
            cur.execute("INSERT INTO test VALUES(default, NOW(), 2)")
            print("Data committed!")
            time.sleep(5)
            continue

    IO.output(18, 0)
    IO.output(18, 1)
    if(IO.input(21) == True):
        with database:
            cur.execute("INSERT INTO test VALUES(default, NOW(), 3)")
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
