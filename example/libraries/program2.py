import utils

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = utils.calculate_area(length, width)
print(f"Area: {area:.2f}")
