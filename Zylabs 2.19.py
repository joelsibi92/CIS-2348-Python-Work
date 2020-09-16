# Joel Sibi
# 1617077

lemon_juice_amnt = float(input('Enter amount of lemon juice (in cups):\n'))
water_amnt = float(input('Enter amount of water (in cups):\n'))
agave_nectar_amnt = float(input('Enter amount of agave nectar (in cups):\n'))
servings_amnt = float(input('How many servings does this make?\n'))

print()

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_amnt), 'servings')
print('{:.2f}'.format(lemon_juice_amnt), 'cup(s) lemon juice')
print('{:.2f}'.format(water_amnt), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_amnt), 'cup(s) agave nectar')

print()

servings_wanted = float(input('How many servings would you like to make?\n'))
servings_scaler = servings_wanted / servings_amnt

print()

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_wanted), 'servings')
print('{:.2f}'.format(lemon_juice_amnt * servings_scaler), 'cup(s) lemon juice')
print('{:.2f}'.format(water_amnt * servings_scaler), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_amnt * servings_scaler), 'cup(s) agave nectar')

print()

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_wanted), 'servings')
print('{:.2f}'.format((lemon_juice_amnt * servings_scaler) /  16), 'gallon(s) lemon juice')
print('{:.2f}'.format((water_amnt * servings_scaler) / 16), 'gallon(s) water')
print('{:.2f}'.format((agave_nectar_amnt * servings_scaler) / 16), 'gallon(s) agave nectar')
