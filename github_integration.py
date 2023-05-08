import datetime as dt

today = dt.date.today()

if today.month == 3 and today.day == 9:
    print('It is my birthday!')

elif today.month == 8 and today.day == 31:
    print("It is Thais' birthday!")
else:
    print("It is neither mine or Thais' birthday")