num  = float(input('Enter the number: '))
unit = input("enter the unit, i for inches, c for centimeters: ")

def convert(num, unit):
    if unit == 'i':
        c = round((num * 2.54), 2)
        print(f'{num} inches equals {c} centimeters.')
    else: 
        i = round((num * 0.3937), 2)
        print(f'f{num} centimeters equals {i} inches.')

convert(num, unit)



