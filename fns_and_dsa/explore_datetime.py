import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().replace(microsecond=0)
    print("Current date and time: " + str(current_date))
    return current_date

current_date = display_current_datetime()

#Prompt the user to enter a number of days (as an integer)

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(current_date, number_of_days):
      future_date = datetime.timedelta(days=number_of_days)
      print("Future date: " + str(current_date + future_date))
calculate_future_date(current_date, number_of_days)

