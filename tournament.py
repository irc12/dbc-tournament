part_array = []

part_amount = int(input("Please enter the number of participants: "))

for i in range(part_amount):
    part_array.append(None)

def slot_assignment(my_array, my_name, my_amount):
	print(f"Desired starting slot #[1-{len(my_array)}]: \n")	
	slot = (int(input("")) - 1)
	while slot not in range(my_amount):
		print(f"That's not an option. Desired starting slot #[1-{len(my_array)}]: ")
		slot = (int(input("")) - 1)
	if my_array[slot] == None:
		my_array[slot] = my_name
		print("Success.")
		print(f"{my_name} is signed up in starting slot #{slot + 1}.\n")
		return my_array
	else:
		print("Slot is already filled.\n")
		slot_assignment(my_array, my_name, my_amount)

def sign_up(array, amount):
	print("Participant Sign Up\n====================\n")
	name = input("Participant Name: ")
	slot_assignment(array, name, amount)	

def cancel(my_amount, my_array):
	print("Participant Cancellation\n========================\n")
	print(f"Starting slot #[1-{len(my_array)}]: ")
	slot = (int(input("")) - 1)
	while slot not in range(my_amount):
		print(f"That's not an option.\nStarting slot #[1-{len(my_array)}]: ")
		slot = (int(input("")) - 1)
	name = input("Participant name: ")
	if name != my_array[slot]:
		print(f"\nError:\n{name} is not in that starting slot.\n")
	else:
		my_array[slot] = '[empty]'
		print(f"Success:\n{name} has been cancelled from starting slot #{slot+1}.\n")

def view_participants(my_amount, my_array):
	print("View Participants\n=================\n")
	print(f"Starting slot #[1-{len(my_array)}]: ")
	slot = (int(input("")) - 1)
	while slot not in range(my_amount):
		print(f"That's not an option.\n Starting slot #[1-{len(my_array)}]: ")
		slot = (int(input("")) - 1)
	print("Starting slot: Participant")
	view_range = 5
	if my_amount <= 10:
		view_range = 2
	for slot in range(slot - view_range, slot + view_range + 1):
		if slot in range(my_amount):
			print(f"{slot+1}:{my_array[slot]}")
	print("\n")

def search(my_amount, my_array):
	print("Search for Participant\n======================\n")
	part = input("Enter Participant's Name:\n")
	part_exists = False
	for i in range(my_amount):
		if my_array[i] == part:
			print(f"\n{part} is in starting position #{i + 1}.\n")
			part_exists = True
	if part_exists == False:
		print(f"\n{part} is not signed up.\n")

def exit_function():
	print("Exit\n")
	print("=====\n")
	print("Are you sure you want to exit?\nAll data will be lost.\n")
	user_exit = input("Exit? [y/n]\n").lower()
	if user_exit == 'y':
		print("Goodbye!")
		exit()

def main_menu():
	print("Participant Menu\n================\n1. Sign Up\n2. Cancel Sign Up" )
	print("3. View Participants\n4. Search for Participant\n5. Exit")
	selection = int(input(""))
	if selection == 1:
		sign_up(part_array, part_amount)
	elif selection == 2:
		cancel(part_amount, part_array)
	elif selection == 3:
		view_participants(part_amount, part_array)
	elif selection == 4:
		search(part_amount, part_array)
	elif selection == 5:
		exit_function()
	else:
		print("Invalid Selection.\n")

while 1 != 0:
	main_menu()