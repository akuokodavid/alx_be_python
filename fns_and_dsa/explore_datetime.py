from datetime import datetime, timedelta, date

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate and display future date
def calculate_future_date(current_date, days_to_add):
    future_date = current_date.date() + datetime.timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main program
current = display_current_datetime()

try:
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current, days)
except ValueError:
    print("Invalid input. Please enter a valid number.")