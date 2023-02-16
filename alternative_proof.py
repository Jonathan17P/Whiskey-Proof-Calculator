# Get inputs from user
current_proof = float(input("What is the current proof of your whiskey? "))
current_volume = float(input("What is the current volume of your whiskey in ml? "))
desired_proof = float(input("What is the desired proof of your whiskey? "))

# Convert proofs to ABV (Alcohol by Volume)
current_abv = current_proof / 2
desired_abv = desired_proof / 2

# Calculate amount of water to add
water_ml = (current_abv / desired_abv - 1) * current_volume

# Print result
print(f"To dilute {current_volume} ml of {current_proof} proof whiskey down to {desired_proof} proof, you need to add {water_ml:.2f} ml of water.")

