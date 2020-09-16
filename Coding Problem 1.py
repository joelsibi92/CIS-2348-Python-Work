# Joel Sibi
# 1617077

print('Birthday Calculator')
print('Current day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Birthday')
birthday_month = int(input('Month: '))
birthday_day = int(input('Day: '))
birthday_year = int(input('Year: '))
if birthday_month >= current_month and birthday_day > current_day:
    dynamic_factor = -1
else:
    dynamic_factor = 0
current_age = current_year - birthday_year
print('You are', current_age + dynamic_factor, 'years old.')
if current_month == birthday_month and current_day == birthday_day:
    print('Happy Birthday!')
