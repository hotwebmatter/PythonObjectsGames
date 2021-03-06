"""Calculate the angle between stars in an aerial firework."""

# Annotate variables
DEGREES_CIRCLE: int = 360
num_stars: int 
angle: float 

# Obtain the number of stars from the user.
num_stars = int(input("How many stars? "))

# Calculate the angle between the stars.
angle = DEGREES_CIRCLE / num_stars

# Tell the user the angle between stars.
print("You will need an angle of " + str(angle)
      + "\u00B0 between each star.")
