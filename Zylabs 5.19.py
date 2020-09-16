# Joel Sibi
# 1617077

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

print()

first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

print()

print('Davy\'s auto shop invoice')

print()

if(first_service != '-'):
    print('Service 1:', first_service, end='')
    print(', $', end='')
    print(services[first_service])
else:
    print('Service 1: No service')

if(second_service != '-'):
    print('Service 2:', second_service, end='')
    print(', $', end='')
    print(services[second_service])
else:
    print('Service 2: No service')

print()

print('Total: $', end='')
print(services[first_service] + services[second_service])

