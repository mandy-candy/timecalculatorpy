#Work time calculator

#Amanda Künzle, 22.07.2019

#--------------------------------------------------#

#https://github.com/mandy-candy/timecalculatorpy.git

#--------------------------------------------------#

import tkinter
import math

#window config
window = Tk()
window.title("TimeCalculator")
#
start_label = Label(window, text="when do you want to start work? for example 07:00")
duration_label1 = Label(window, text="how long do you want to work? for example: 08:15")



breakTime = 0.25
lunchBreak = 0.25

#start time input and calculation
startTime = input("Enter your start time in format 7:00 for example   ")
#startTime = "07:22"

startTimeList = startTime.split(':')

calculatedStartTime = float(startTimeList[0]) + float(startTimeList[1]) / 60

#print("your start time is   ", round(calculatedStartTime, 2))

#work time input and calculation
workingTime = input("How many hours do you want to work? enter in format 8:15 for example   ")
#workingTime = "06:30"

workingTimeList = workingTime.split(':')

calculateWorkTime = breakTime + lunchBreak + float(workingTimeList[0]) + float(workingTimeList[1]) / 60

print("Your target working time is (with break):   ", round(calculateWorkTime, 2))

calculatedEndTimeDecimal = calculatedStartTime + calculateWorkTime

#print("you can finish work at   ", round(calculatedEndTimeDecimal, 2))

calculatedEndTime = math.modf(calculatedEndTimeDecimal)

calculatedEndHours = calculatedEndTime[1]
calculatedEndMinutes = calculatedEndTime[0] * 60 / 100

#print(calculatedEndHours)
#print(round(calculatedEndMinutes, 2))

EndTime = calculatedEndHours + round(calculatedEndMinutes, 2)

print("You can finish work at:   ", EndTime)




