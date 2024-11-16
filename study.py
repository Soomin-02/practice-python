user_choice = int(input("Choice number."))
pc_choice = 20

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higher!")
