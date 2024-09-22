def greet(name):
  """Greets someone by name."""
  print(f"Hello, {name}!")

def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  area = length * width
  return area

def convert_celsius_to_fahrenheit(celsius):
  """Converts Celsius temperature to Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def roll_dice(sides):
  """Simulates rolling a dice with a given number of sides."""
  import random
  return random.randint(1, sides)

# Simple tests for each function
def test_greet():
  expected_output = "Hello, Alice!"
  actual_output = greet("Alice")
  #assert expected_output == actual_output, "greet function failed"

def test_calculate_area():
  expected_output = 20
  actual_output = calculate_area(4, 5)
  assert expected_output == actual_output, "calculate_area function failed"

def test_convert_celsius_to_fahrenheit():
  expected_output = 89.6
  actual_output = convert_celsius_to_fahrenheit(32)
  assert abs(expected_output - actual_output) < 0.1, "convert_celsius_to_fahrenheit function failed"

def test_roll_dice():
  expected_output_in_range = True
  actual_output = roll_dice(6)
  assert 1 <= actual_output <= 6, "roll_dice function failed (out of range)"

# Run tests only if the file is executed directly
if __name__ == "__main__":
  test_greet()
  test_calculate_area()
  test_convert_celsius_to_fahrenheit()
  test_roll_dice()
  print("All tests passed!")
