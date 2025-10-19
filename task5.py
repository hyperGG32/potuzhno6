def is_leap(year: int) -> bool:
    """Returns whether the year is leap or not"""
    return year % 4 == 0 and year % 100 != 0

def days_in_month(month: int, year: int) -> int:
    """Returns count of days in month"""
    if is_leap(year):
        return (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[month-1]
    return (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[month-1]

def next_month(month: int, year: int) -> tuple[int, int]:
    """Switch to next month, automaticly changes year
    Returns a tuple (month, year)"""
    month += 1
    if month == 13:
        year += 1
        month = 1
    return month, year

mn = int(input("Input month as int pls: "))
yr = int(input("Input year as int pls: "))

lsofmonthsintext = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for i in range(3):
    print(lsofmonthsintext[mn-1], yr,'-', days_in_month(mn, yr), "days")
    mn, yr = next_month(mn, yr)
print(f"(Leap year): {"Yes" if is_leap(yr) else "No"}")
