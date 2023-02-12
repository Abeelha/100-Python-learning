# Theodoro Bertol Dev (Abeelha) #
# || Day 10 of #100DaysOfCode || #


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# The List month_days contains the number of days in a month from January to December for a non-leap year.
# A leap year has 29 days in February.
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if month > 12 or month < 1:
      return "Invalid Month"
  
  call_leap_year = is_leap(year)
  
  if call_leap_year == True and month == 2:
      return 29
  else:
      return month_days[month - 1]
   
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
