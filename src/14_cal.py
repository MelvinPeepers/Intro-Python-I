"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

UPER

## Understand
https://www.pythonforbeginners.com/system/python-sys-argv
"With the len(sys.argv) function you can count the number of arguments."
https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv
https://www.geeksforgeeks.org/calendar-in-python/

conditional statements in Python
https://www.digitalocean.com/community/tutorials/how-to-write-conditional-statements-in-python-3-2"

##
** Plan
Code itself is the Execute
Reflect

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:

 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
   **
    if no input: print datetime current month - this will go last if none of the conditions are meet.
   **

 - elif the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
   **
   if len(sys.argv) == 1 datetime month - this will go first - if user specifies 1 argument print calendar for that month and current year.
   **

 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
  **
  elif len(sys.argv) == 2 datetime month year - if users specifies 2 arguments print calander for that month and year.
  **

 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
   ** else

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# d = datetime.today()
# y = (d.year)
# m = (d.month)

# #print(len(sys.argv))

# if len(sys.argv) == 1:
#     print(calendar.month(y, m))
# elif len(sys.argv) == 2:
#     print(calendar.month(y, int(sys.argv[1])))
# elif len(sys.argv) == 3:
#     print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
# else:
#     print('Program expects arguments to be given [month] [year]')

# following Brady Fukumoto solution for better understanding in his Intro to Python II CS26 video
# https://www.youtube.com/watch?v=47thb9kJ5Cg&feature=youtu.be
# my own thoughts, I like how he explained his plan and explained everything at execution.
# Also watching him code it gave me a better understanding of the tools that are available in Python (like dir(calendar))

args = sys.argv  # we need to get our args
# print(args)  # to see what we get in our args (troubleshooting)

# if no args are supplied…
if len(args) == 1:  # <— no args are supplied
    # Print a text calendar for current month and year
    month = datetime.today().month
    year = datetime.today().year
    calendar.prmonth(year, month)
# if 1 arg is supplied…
elif len(args) == 2:
    # check if it’s an int 1 - 12, print out calendar for that month, current year
    month = int(args[1])
    year = datetime.today().year
    calendar.prmonth(year, month)
# if 2 args are supplied…
elif len(args) == 3:
    # check If 1 is int 1 - 12, check if 2 is an int
    # print out calendar for that month and year
    month = int(args[1])
    year = int(args[2])
    calendar.prmonth(year, month)
# Otherwise, print an error with usage hint
else:
    print("Error: Commands must be in the form `14_cal.py [month] [year]`")
