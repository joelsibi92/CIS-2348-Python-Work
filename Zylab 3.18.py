# Joel Sibi
# 1617077
import math

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
gallons_needed = (wall_height * wall_width) / 350
paint_cans = int(math.ceil(gallons_needed))
paints_list = {'red':35, 'blue':25, 'green':23}

print('Wall area:', wall_width * wall_height, 'square feet')
print('Paint needed: {} gallons'.format('{:.2f}'.format(gallons_needed)))
print('Cans needed:', paint_cans, 'can(s)')
print()

paint_selection = str(input('Choose a color to paint the wall:\n'))
print('Cost of purchasing', paint_selection, 'paint: $', end='')
print(paints_list[paint_selection] * paint_cans)



