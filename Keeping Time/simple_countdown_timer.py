"""
Simple Countdown Program:

Write a countdown program that measures how long this piece of code takes to run.
Count down from 60.
Pause for one second in between displaying each number in the countdown by calling time.sleep().
Print the time your code takes to run at the end of the countdown.
"""
import time


def countdown_timer(value):
    print("Starting now:")
    for i in range(value, 0, -1):
        print(i)
        time.sleep(1)
    print("Times up!")


print("Lets start a timer!")
value = input("Please enter time in seconds: ")
startTime = round(time.time())
countdown_timer(int(value))
endTime = round(time.time())
print('This process took %s seconds long.' % (endTime - startTime))
