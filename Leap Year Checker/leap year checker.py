def is_leap_year(year):
    if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('It\'s leap year!')
    else:
        print('Not a Leap Year')

is_leap_year(2024)