# Our function will take three parameters:
# last - The Date object with the date of the last period
# today - The Date object with the date of the check
# cycleLength - Integer representing the length of the cycle in days
# If the today is later from last than the cycleLength, the function should return true.
# We consider it to be late if the number of passed days is larger than the cycleLength.
# Otherwise return false.

from datetime import date, timedelta


def period_is_late(last, today, cycle_length):
    return today - last > timedelta(days=cycle_length)


# tests
print("Basic tests")
print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False)
print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28) == True)
print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False)
print(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28) == False)
print(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28) == False)
print(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28) == True)
print(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30) == True)
print(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30) == False)
print(period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30) == False)
print(period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30) == True)

# other soluce
# def period_is_late(last, today, cycle_length):
#     return (today - last).days > cycle_length
# OR
# period_is_late = lambda l,t,c: abs((t-l).days)>c
