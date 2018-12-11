import RPi.GPIO as IO
import MySQLdb as db
import time
import sys

# Startup configuration
IO.setwarnings(False)
IO.cleanup() # Clear pins
IO.setmode(IO.BCM) # Broadcom GPIO pin mapping

# Input pins
IO.setup(17, IO.IN) # Echo 1
IO.setup(23, IO.IN) # Echo 2
IO.setup(5, IO.IN)  # Echo 3
IO.setup(4, IO.IN, pull_up_down=IO.PUD_UP) # Restart button

# Output pins
IO.setup(27, IO.OUT) # Trigger 1
IO.setup(24, IO.OUT) # Trigger 2
IO.setup(6, IO.OUT)  # Trigger 3
IO.setup(16, IO.OUT) # Mat

# Database connection
database = db.connect('localhost', 'monitor', 'password', 'packages')
cur = database.cursor()

print("Starting system...")

# Activate outputs
# Pins 27, 24 and 6 are disabled
# Pin 16 is enabled for mat operation
IO.output(27, 0)
IO.output(24, 0)
IO.output(6, 0)
IO.output(16, 1)
time.sleep(2)

# Global variables
global x
global pulse_start_time
global pulse_end_time
global pulse_duration
global distance

x = 0
time.sleep(2)
while 1:
    # System interruption
    # Shutdown occurs after 10 failed detection attempts
    if(x == 10):
        IO.output(16, 0) # Mat disabled
        print("Halting...")
        time.sleep(2)
        while 1:
            if(IO.input(4) == False): # Button input detection
                IO.output(16, 1) # Mat enabled
                break
            time.sleep(0.2)
        x = 0
        print("Restarting...")
    
    time.sleep(2)
    IO.output(27, 1) # Enable signal to trigger
    time.sleep(0.00001) # Sleep for 0.01ms
    IO.output(27, 0) # Disable signal to trigger
    while IO.input(17) == 0:
        pulse_start_time = time.time() # Start time of signal
    while IO.input(17) == 1:
        pulse_end_time = time.time() # Arrival time of reflected signal
    pulse_duration = pulse_end_time - pulse_start_time # Difference between start and arrival
    distance = round(pulse_duration * 17150, 2) # Distance calculated in cm
    if(distance < 50):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 1)")
            print("Data committed for floor 1!")
            x = 0
            time.sleep(2)
            continue

    time.sleep(2)
    IO.output(24, 1)
    time.sleep(0.00001)
    IO.output(24, 0)
    while IO.input(23) == 0:
        pulse_start_time = time.time()
    while IO.input(23) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    if(distance < 50):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 2)")
            print("Data committed for floor 2!")
            x = 0
            time.sleep(2)
            continue

    time.sleep(2)
    IO.output(6, 1)
    time.sleep(0.00001)
    IO.output(6, 0)
    while IO.input(5) == 0:
        pulse_start_time = time.time()
    while IO.input(5) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    if(distance < 50):
        with database:
            cur.execute("INSERT INTO log VALUES(default, NOW(), 3)")
            print("Data committed for floor 3!")
            x = 0
            time.sleep(2)
            continue

    else:
        print("Nothing detected on sensors!")
        x = x + 1
        time.sleep(2)
        continue

#Close database connection
print("Closing database...")
database.close()
time.sleep(2)

print("Shutting down system...")
time.sleep(5)
sys.exit()

