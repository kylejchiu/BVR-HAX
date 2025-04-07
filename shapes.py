def calculate_area(shape, length, height):
    if shape == "circle":
        area = 3.14159 * length**2 / 4
    elif shape == "square":
        area = length**2
    elif shape == "rectangle":
        area = length * height
    elif shape == "triangle":
        area = length * height / 2
    else:
        print("Invalid shape")
    return area

shape = input("Enter your shape: ")
length = float(input("Enter your length: "))
height = float(input("Enter your height: "))
print(calculate_area(shape, length, height))