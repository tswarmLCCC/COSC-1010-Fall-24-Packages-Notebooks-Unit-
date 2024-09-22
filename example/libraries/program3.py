import utils

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = utils.convert_celsius_to_fahrenheit(celsius)
print(f"{celsius:.2f} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")
