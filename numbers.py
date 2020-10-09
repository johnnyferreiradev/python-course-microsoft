# check if the type is a number
def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

pi = 3.14159
print(pi)

first_number = 3
second_number = 7

print(first_number + second_number)
print(first_number ** second_number)

days_in_feb = 28
print(str(days_in_feb) + ' days in February')

first_input = input('Enter first number: ')
second_input = input('Enter second number: ')

if (not isnumber(first_input) and not isnumber(second_input)):
    print('Entou aqui')
    first_input = 0
    second_input = 0

print(float(first_input) + float(second_input))
print(int(first_input) + int(second_input))
