validity = False
hrValid = False
minValid = False

aOrp = 0
timeList= []

while not validity:
    aOrp = input("Is the time in AM or PM?").lower()
    if aOrp == "am":
        aOrp = 1
        validity = True
    elif aOrp == "pm":
        aOrp = 2
        validity = True
    else:
        print("Invalid Input")

while not hrValid:
    hour = int(input("What value is the hour?"))
    if 9 >= hour >= 1:
        if aOrp == 1:
            timeList.append(0), timeList.append(hour)
            hrValid = True
        elif aOrp == 2:
            hour = str(hour * 100 + 1200)
            timeList.append(hour[0]), timeList.append(hour[1])
            hrValid = True
    elif 12>= hour >= 10:
        if aOrp == 1:
            if hour == 12:
                timeList.append(0), timeList.append(0)
                hrValid = True
            else:
                hour = str(hour)
                timeList.append(hour[0]), timeList.append(hour[1])
                hrValid = True
        if aOrp == 2:
            if hour == 12:
                hour = str(hour)
                timeList.append(hour[0]), timeList.append(hour[1])
                hrValid = True
            else:
                hour = str(hour * 100 + 1200)
                timeList.append(hour[0]), timeList.append(hour[1])
                hrValid = True
    else:
        print("Invalid Input")

while not minValid:
    minute = int(input("What value is the minute?"))
    if 9 >= minute >= 0:
        timeList.append(0), timeList.append(minute)
        minValid = True
    elif 59 >= minute >= 10:
        minute = str(minute)
        timeList.append(minute[0]), timeList.append(minute[1])
        minValid = True
    else:
        print("Invalid Input")


print ("The military time is : ", end="")
for i in timeList:
    print(i, end="")