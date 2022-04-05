# This is a Python comment in my first Python app.
from itertools import count
import math
from re import M
import string
import datetime as dt
from time import time
from tkinter import Y
from unittest import case
from dateutil.tz import gettz

from matplotlib import dates
# This variable contains an integer
quantity = 10

# This variable contian float
unit_price = 1.99

# This quantity contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price

# Show the results
print(extended_price)

# This variable contains an integer
quantity = 14

# This variable contian float
unit_price = 26.99

# This quantity contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price

# Show the results
print(extended_price)

first_name = "Alan"
last_name = "Simpson"
print(first_name, last_name)

# first_name = "Alan"; last_name = "Simpson" 
# print(last_name, first_name)

# first_name = "Alan"; last_name = "Simpson"; print(first_name, last_name)

x = 1
if x == 2:
    print("x is 2")
else:
    print("x is", x)
print("All done")

x = -5
y = abs(x)
print(x)
print(y)

x = 1.23456789012345679800000001
y = round(x, 2)
print(x)
print(y)

pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454
print(pi)
print(e)
print(tau)
print(math.sqrt(x))
print(math.factorial(y))
print(math.floor(z))
print(math.degrees(y))
print(math.radians(45))

username = "Ayo"
print(f"Hello {username}")

unit_price = 49.99
quantity = 30
print(F"Subtotal: ${quantity * unit_price}")
print(f"Subtotal: ${quantity * unit_price:,}")
print(f"Subtotal: ${quantity * unit_price:,.4f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(F"Sales Tax Rate {sales_tax_rate:.5%}")

sample1 = f"Sales Tax Rate {sales_tax_rate:.2%}"
sample2 = f'Sales Tax Rate {sales_tax_rate:.4%}'
sample3 = f"""Sales Tax Rate {sales_tax_rate:.8%}"""
sample4 = F'''Sales Tax Rate {sales_tax_rate:.1%}'''

print(sample2)
print(sample2)
print(sample3)
print(sample4)

# Making multiline break in format string
user1 = "Adeyemi"
user2 = "Bimbo"
user3 = "Kashimawo"
output = f"{user1} /n{user2} /n{user3}"
print(output)

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal: ${subtotal:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total: ${total:,.2f}
"""
print(output)

# All dollar amounts are right aligned within a width of 9 characters (>9)
unit_price = 49.95
qunatity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:>9,.2f}
Sales Tax: ${sales_tax:>9,.2f}
Total:     ${total:>9,.2%}
"""
print(output)

s_subtotal = "$" + f"{subtotal:,.2f}"

# All the dollar amounts neatly aligned.
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"
output = f"""
Subtotal:  {s_subtotal:>9}
Sales Tax: {s_sales_tax:>9}
Total:     {s_total:>9}
"""
print(output)

# Concatenating string without space
first_name = "Aremu"
middle_init = "C"
last_name = "Asiwaju"
full_name = first_name+middle_init + last_name
print(full_name)

# Contatenation with space inbetween
full_name = first_name + " " + middle_init + " " + last_name
print(full_name)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

s1 = "There is no such word as schmeedledorp"
s2 = "   a b c   "
s3 = "ABC"
# Capitalize first letter, the rest lowercase
print(s3.capitalize())
# Count the number of spaces in s1
print(s1.count(" "))
# Find the number of dot in s4
# print(s4.find("."))
# Is s2 all lowercase letters
print(s2.islower())
# Convert s3 to all lowercase
print(s3.lower())
# String leading characters from s2
print(s2.lstrip())
# String leading and trailing characters from s2
print(s2.strip())
# Swap the case of letters in s1
print(s1.swapcase())
# Show s1 in title case (initial caps)
print(s1.title())
# Show s1 uppercase
print(s1.upper())

# Import the datetime module, nickname dt
# Store today's date in a variable named today
today = dt.date.today()
# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019, 12, 31)

print(today)
print(last_of_teens)

# Isolate any part of date object
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

# Format the date output
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m%d%Y}"

right_now = dt.datetime.now()
print(right_now) 

new_years_eve = dt.datetime(2019, 12, 31, 23, 59)
print(new_years_eve)

# Number of days between two dates
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)

duration = dt.timedelta(days=146)
print(new_years_day + duration)
print(new_years_day - duration)

start_time = dt.datetime(2019, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2019, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))

# Calculate age, subtracting birthdate from the current time, now
now = dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
age = now - birthdatetime
print(age)
print(type(age))

# Using birthday of Jan 31 2000
today = dt.date.today()
birthdate = dt.date(2000, 12, 31)
delta_age = birthdate - today
print(delta_age)

delta_age = (today - birthdate)
days_old = delta_age.days
print(days_old, type(days_old))

year_old = days_old // 365
print(year_old)

# Get the time from the computer clock
here_now = dt.datetime.now()

# Get the UTC datetime right now
utc_now = dt.datetime.utcnow()

# Subtract to see difference
time_difference = (utc_now - here_now)

print(f"My Time    : {here_now:%I:%M %p}")
print(f"My Time    : {utc_now:%I:%M %p}")
print(f"My Time    : {time_difference}")

time_difference = (here_now - utc_now)
print(time_difference)
time_difference = (utc_now - here_now)
print(time_difference)

# UTC time right now
utc = dt.datetime.now(gettz("Etc/UTC"))
print(f"{utc:%A %D %I:%M %p %Z}")

# USA Easter time
est = dt.datetime.now(gettz('America/New_York'))
print(f"{est:%A %D %I:%M %p %Z}")

# USA Central time
cst = dt.datetime.now(gettz("America/Chicago"))
print(f"{cst:%A %D %I:%M %p %Z}")

# USA Mountain time
mst = dt.datetime.now(gettz("America/Boise"))
print(f"{mst:%A %D %I:%M %p %Z}")

pst = dt.datetime.now(gettz("America/Los_Angelis"))
print(f"{pst:%A %D %I:%M %p %Z}")

# July 4 Event, 7:00 local time (no specific time zone)
event = dt.datetime(2020, 7, 4, 19, 0, 0)
# Show local date and time
print("Local: " + f"{event:%D %I:%M %p %Z}" + "\n")

event_eastern = event.astimezone(gettz("America/New_York"))
print(f"{event_eastern:%D %I:%M %p %Z}")

event_central = event.astimezone(gettz("America/Chicago"))
print(f"{event_central:%D %I:%M %p %Z}")

event_mountain = event.astimezone(gettz("America/Denver"))
print(f"{event_mountain:%D %I:%M %p %Z}")

event_pacific = event.astimezone(gettz("America/Los_Angelis"))
print(f"{event_pacific:%D %I:%M %p %Z}")

event_utc = event.astimezone(gettz("Etc/UTC"))
print(f"{event_utc:%D %I:%M %p %Z}")