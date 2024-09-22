import utils

sides = int(input("Enter the number of sides on the dice: "))
result = utils.roll_dice(sides)
print(f"You rolled a {result}!")
