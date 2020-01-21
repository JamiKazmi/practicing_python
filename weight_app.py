weight = int(input('Weight : '))
unit = input('(l)bs or (k)gs: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'Your weight is {converted} kg\'s.')
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f'Your weight is {converted} lb\'s')
else:
    print('Oops..! Wrong choice')
