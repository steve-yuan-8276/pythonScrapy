import math

a = float(input('Enter a number:'))
b = float(input('Enter a number:'))
c = float(input('Enter a number:'))

if a + b > c and a + c > b and c + b > a:
    p = a + b + c
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'The circumference is {p}, and area is {area:.1f}.')
else:
    print("Sorry, this isn't a triangle.") 

