def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        print('Yeah, this is a leap year.')
    else:
        print('Not a leap year!')

year = int(input('Enter a year: '))
leap_year(year)
