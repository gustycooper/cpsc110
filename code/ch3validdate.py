dateStr = input("Enter a date (mm/dd/yyyy): ")

monthStr, dayStr, yearStr = dateStr.split("/")
month = int(monthStr)
day = int(dayStr)
year = int(yearStr)

goodmonth = True
if month < 1 or month > 12:
    goodmonth = False

goodday = True
if day < 1 or day > 31:
    goodday = False
elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
    goodday = False
elif month == 2 and day > 28:
    goodday = False

if goodmonth and goodday:        
    season = "Spring"
    if (month == 6 and day >= 21) or month == 7 or month == 8 or (month == 9 and day <= 21):
        season = "Summer"
    elif (month == 9 and day >= 22) or month == 10 or month == 11 or (month == 12 and day <= 20):
        season = "Fall"
    elif (month == 12 and day >=21 ) or month == 1 or month == 2 or (month == 3 and day <= 19):
        season = "Winter"
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthStr = months[month-1]
    print(monthStr, dayStr+",", yearStr, "is valid and in", season)
else:
    print("Invalid date!")
