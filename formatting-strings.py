first_name = 'Johnny'
last_name = 'Ferreira'

output = 'Hello, ' + first_name + ' ' + last_name
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {1} {0}'.format(first_name, last_name)

# Only available in Python 3 
output = f'Hello, {first_name} {last_name}'

print(output)