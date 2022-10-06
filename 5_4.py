alien_colors = ['green', 'yellow', 'red']
print("Guess the color of the alien?")
alien_colors = input()

if 'green' in alien_colors:
    print("You earned 5 points.")
if 'red' in alien_colors:
    print("You earned 10.")
if 'yellow' in alien_colors:
    print("You earned 15 points")