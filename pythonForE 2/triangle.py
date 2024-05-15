def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
a = int(input('Enter a integer: '))
b = int(input('Enter a integer: '))
c = int(input('Enter a integer: '))

if triangle(a, b, c):
    print('This is a triangle.')
else:
    print('No, This isn\'t a triangle.')
