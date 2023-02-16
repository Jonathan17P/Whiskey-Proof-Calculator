def calculate_new_proof(original_proof, original_volume, final_volume):
  return original_proof * (original_volume / final_volume)

original_proof = float(input("Enter the original proof of the whiskey: "))
original_volume = float(input("Enter the original volume of the whiskey: "))
final_volume = float(input("Enter the final volume of the whiskey after adding water: "))

new_proof = calculate_new_proof(original_proof, original_volume, final_volume)

print("The new proof of the whiskey is:", new_proof)

