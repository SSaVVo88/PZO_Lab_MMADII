from datetime import date, timedelta

print ("Hello World")

ulams_birthdate = date(1909, 4, 23 )

print("number od days since Ulam's birthday: ",(date.today() - ulams_birthdate).days)

year = int(input("enter your birth year: "))
month = int(input("enter your birth month: "))
day = int(input("etner your birth day: "))

print("your birthday is: " + str(day) + "." + str(month) + "." + str(year))