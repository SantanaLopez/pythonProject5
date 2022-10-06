requested_toppings = ['mushrooms', 'chicken', 'extra sauce']
for requested_topping in requested_toppings:
    if requested_topping == 'chicken':
        print("Sorry we are out of chicken right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza")
