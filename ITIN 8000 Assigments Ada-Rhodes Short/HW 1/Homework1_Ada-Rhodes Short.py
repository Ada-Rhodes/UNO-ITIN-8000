"""This is my code for homework 1 for ITIN 8000,
it will print a statement containing the date and some additional information
This work was done by Dr. Ada-Rhodes Short in Fall of 2021"""
from datetime import datetime

# Get the timestamp for today
today = datetime.now()

# Extract the month name from todays date as a string and store as a variable for later
month_name = today.strftime("%B")
# Extract month Number
month_number = today.month

# Extract the day of the month as a number from today's date
day_number = today.day

# If the day is equal to 1, 21, or 31 define suffix variable as "st"
if day_number == 1 or 21 or 31:
    suffix = "st"
# If the day is 2 or 22 define the suffix variable as "nd"
elif day_number == 2 or 22:
    suffix = "nd"
# If the day is equal to 3 or 23 define the suffix variable as "rd"
elif day_number == 3 or 23:
    suffix = "rd"
# If else then define the suffix variable as "th"
else:
    suffix = "th"

# Extract the year as a number from todays date

# If the day numbers modulus of 2 is zero (it is even) and define day_type as "even"
# else define day_type as "odd"

# print the "Hello..." statement with appropriate variables in place
# Create a new line to print to

# Print "if you counted..." statement"

# LOOP
# Define n=1
# WHILE n>=day_number
# print n + a new line
# n=n+1
# END LOOP

# Print "days"
