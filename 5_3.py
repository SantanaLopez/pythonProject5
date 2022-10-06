alien_colors = ['green', 'yellow', 'red']
print("Guess the color of the alien?")
alien_colors = input()

if 'green' in alien_colors:
    points = 5
elif 'red' in alien_colors:
    points = 10
elif 'yellow' in alien_colors:
    points = 15
print("You earned " + str(points) + " points.")

