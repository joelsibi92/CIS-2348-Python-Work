#Joel Sibi
#1617077

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError as excpt:
        print('{} {}'.format(name, 0))
        # Get next line
    parts = input().split()
    name = parts[0]