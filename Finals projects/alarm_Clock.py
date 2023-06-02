monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 6
vacation = False

alarm = 0

print("Are you on vacation?")
trip = input()
if trip == "true" or trip == "yes":
    vacation = True
else:
    vacation = False

print("What day is it?")
date = input()

if date == "monday":
    Date = monday
elif date == "tuesday":
    Date = tuesday
elif date == "wednesday":
    Date = wednesday
elif date == "thursday":
    Date = thursday
elif date == "friday":
    Date = friday
elif date == "saturday" or date == "sunday":
    Date = saturday
else:
    print('That is not a valid day')

if 1 <= Date <= 5 and vacation == False:
    alarm = 1
elif 1 <= Date <= 5 and vacation == True:
    alarm = 2
elif Date == 6 and vacation == False:
    alarm = 3
elif Date == 6 and vacation == True:
    alarm = 0

if alarm == 1:
    print("Your alarm is set for 7:00 AM")
elif alarm == 2 or alarm == 3:
    print("Your alarm is set for 10:00 AM")
else:
    print("Your alarm is off")
