length = int(input("Please input the length(cm): "))
width = int(input("Please input the width(cm): "))

def area_of_the_rectangle(length, width):
    area_of_the_rectangle = length * width
    return area_of_the_rectangle

def perimeter_of_the_rectangle(length, width):
    perimeter_of_the_rectangle = (length + width)*2
    return perimeter_of_the_rectangle

print(f"The area of the rectangle is {area_of_the_rectangle(length, width)} cm² .")
print(f"The perimeter of rhe rectangle is {perimeter_of_the_rectangle(length, width)} cm.")