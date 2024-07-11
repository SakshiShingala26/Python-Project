"""Python program capable to grtting you with Good Morninh , Good Afternoon , Good Evening .
use time modeule to get current Hour .

It wishing to us at current time of our system.
"""

import time 
t = time.strftime("%H:%M:%S")
hour = int(time.strftime(" %H "))

name = input("Enter Your Name ::-")
if (hour >= 0 and hour <= 12):
    print(f"Current time is {hour}\nGood Morning {name}..")
    
elif (hour >= 12 and hour <=17):
    print(f"Current time is {hour}\nGood Afternoon {name}..")   
    
elif (hour >= 17 and hour <= 22):
    print(f"Current time is {hour}\nGood Evening {name}..")
    
elif (hour >= 22 and hour < 0):
    print(f"Current time is {hour}\nGood Night {name}..")
