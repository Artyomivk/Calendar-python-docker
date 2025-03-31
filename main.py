import calendar 

print('Welcome to the best calendar\n')

year = int(input('Please write year: '))
month = int(input('Please write number of mounth: '))

print(calendar.month(year, month))

print('Good luck!')