import RPi.GPIO as IO
import MySQLdb as db
import time
import sys

#Startup and configuration pins
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(16,IO.IN)
IO.setup(20,IO.IN)
IO.setup(21,IO.IN)

print("Starting system...")

#Database configuration/connection
database = db.connect('localhost', 'monitor', 'password', 'packages')
cur = database.cursor()

time.sleep(10)
x = 0
while x != 10:
    #Checks if GPIO pins received any signal
    #Shutdown occurs after 10 failed detection attempts
    if(IO.input(16)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 1)")
            print("Data committed!")
            time.sleep(5)
            continue
    if(IO.input(20)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 2)")
            print("Data committed!")
            time.sleep(5)
            continue
    if(IO.input(21)==True):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 3)")
            print("Data committed!")
            time.sleep(5)
            continue
    else:
        print("Nothing detected on sensors!")
        x = x + 1
        time.sleep(5)

#Close database connection
print("Closing database...")
database.close()
time.sleep(3)
print("Shutting down system...")
time.sleep(3)
sys.exit()
