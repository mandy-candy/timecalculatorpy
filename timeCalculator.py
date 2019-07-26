#Work time calculator

#Amanda Künzle, 22.07.2019

#--------------------------------------------------#

#https://github.com/mandy-candy/timecalculatorpy.git

#--------------------------------------------------#
from tkinter import*
import math

#button action

def button_action():
    entry_text = EndTime.get()
    if (entry_text == ""):
        welcome_label.config(text="Please enter Time firstly.")
    else:
        entry_text = "You can finish work at: " + entry_text + "!" 
        welcome_label.config(text=entry_text)
        
#window config
window = Tk()
window.title("TimeCalculator")
#labels
start_label = Label(window, text="when do you want to start work? for example 07:00")
duration_label1 = Label(window, text="how long do you want to work? for example: 08:15")
welcome_label = Label(window)

#input
startTime = Entry(window, bd=5, width=10)
workTime = Entry(window, bd=5, width=10)

#buttons
welcom_button = Button(window, text="calculate", command=button_action)
exit_button = Button(window, text="exit", command=window.quit)

# window follow up
start_label.grid(row = 0, column = 0)
duration_label1.grid(row = 1, column = 0)
startTime.grid(row = 0, column = 1)
workTime.grid(row = 1, column = 1)
welcom_button.grid(row = 2, column = 0)
exit_button.grid(row = 2, column = 1)
welcome_label.grid(row = 3, column = 0, columnspan = 3)



mainloop()


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




