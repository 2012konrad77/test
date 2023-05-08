import datetime as dt

today = dt.date.today()

if today.month == 3 and today.day == 9:
    print('It is my birthday!')
elif today.month == 8 and today.day == 31:
    print("It is Thais' birthday!")
elif today.month == 6 and today.day == 18:
    print("It is Pedro's birthday!")
elif today.month == 4 and today.day == 26:
    print("It is Thomas' birthday!")
else:
    print("Today is neither mine, Thais', Pedro's or Thomas' birthday")