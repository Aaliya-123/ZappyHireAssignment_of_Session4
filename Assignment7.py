import datetime
birthdate = input("Enter your birth year in DD-MM-YY format : ")
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print(f"Your age is {age} years.")