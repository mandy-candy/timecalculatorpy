#Work time calculator

import math

breakTime = 0.25
lunchBreak = 0.25

#start time input and calculation
startTime = input("enter your start time in format 7:00 for example   ")
#startTime = "07:22"

startTimeList = startTime.split(':')

calculatedStartTime = float(startTimeList[0]) + float(startTimeList[1]) / 60

print("your start time is", round(calculatedStartTime, 2))

#work time input and calculation
workingTime = input("how many hours do you want to work? enter in format 8:15 for example   ")
#workingTime = "08:30"

workingTimeList = workingTime.split(':')

calculateWorkTime = breakTime + lunchBreak + float(workingTimeList[0]) + float(workingTimeList[1]) / 60

print("your target working time is (with break)  ", calculateWorkTime)


calculatedEndTimeDecimal = calculatedStartTime + calculateWorkTime

print("you can finish work at", round(calculatedEndTimeDecimal, 2))


calculatedEndTime = math.modf(calculatedEndTimeDecimal)

calculatedEndHours = calculatedEndTime[1]
calculatedEndMinutes = calculatedEndTime[0] * 60 / 100

#print(calculatedEndHours)
print(round(calculatedEndMinutes, 2))

EndTime = calculatedEndHours + round(calculatedEndMinutes, 2)

print(EndTime)




