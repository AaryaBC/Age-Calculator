import datetime
a = datetime.datetime.now()

def AgeCalculator(month, day, year):

    if (user_month > 12 or user_month < 1):
        print("Enter a valid month")
    
    elif (a.month < user_month):

        month = 12 + (a.month - user_month)
        year = a.year - user_year - 1

        if (a.day <= user_day):
            day = user_day - a.day

        elif (a.day >= user_day):
            day = a.day - user_day

        else:
            print("Enter a valid date")

    elif(a.month >= user_month): 

        if (a.month == user_month):

            if a.day >= user_day:
                month = 0
                year = a.year - user_year

            else:
                month = 11
                year = a.year - user_year - 1

        else:
            month = a.month - user_month
            year = a.year - user_year

        if (user_day > 31 or user_day < 1):
            print("Enter a valid date")

        elif (a.day < user_day):
            day = 30 - (user_day - a.day)

        elif (a.day >= user_day):
            day = a.day - user_day

    print("Your current age is",year," years,",month," month and",day," days.")         
               

user_month = int(input("Enter the month: "))
user_day = int(input("Enter the day: "))
user_year = int(input("Enter the year: "))

AgeCalculator(0, 0, 0)



