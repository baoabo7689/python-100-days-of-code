print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("left or right? ").strip().lower()

if direction == "left":
	action = input("swim or wait? ").strip().lower()

	if action == "wait":
		door = input("Which door? Red, Blue, or Yellow? ").strip().lower()

		if door == "red":
			print("Burned by fire. Game Over.")
		elif door == "blue":
			print("Eaten by beasts. Game Over.")
		elif door == "yellow":
			print("You Win!")
		else:
			print("Game Over.")
	else:
		print("Attacked by trout. Game Over.")
else:
	print("Fall into a hole. Game Over.")
