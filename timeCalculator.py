#Work time calculator

import math

breakTime = 0.25

#start time input and calculation
startTime = input("enter your start time in format 7:00 for example   ")

startTimeList = startTime.split(':')

calculatedStartTime = float(startTimeList[0]) + float(startTimeList[1]) / 60

print("your start time is", calculatedStartTime)

#work time input and calculation
workingTime = input("how many hours do you want to work? enter in format 8:15 for example   ")

workingTimeList = workingTime.split(':')

calculateWorkTime = float(workingTimeList[0]) + float(workingTimeList[1]) / 60

print("your target working time is (with break)  ", calculateWorkTime)


calculatedEndTimeDecimal = calculatedStartTime + calculateWorkTime

print("you can finish work at", calculatedEndTimeDecimal)


calculatedEndTime = math.modf(calculatedEndTimeDecimal)

print(calculatedEndTime)



