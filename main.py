import random

main_matrix = [[random.randint(0,9) for _ in range(4)] for _ in range(4)]
for row in main_matrix:
    print(row)

while True:
    print("\nSelect 1 if you want to add a new row with random numbers."
          "\nSelect 2 if you want to add a new column with random numbers."
          "\nSelect 3 if you want to select an number and change the number value."
          "\nSelect 4 if you want to replace the selected number with an empty value.")

    choice = input("Make your choice(1/2/3/4): ")

    if choice == "1":
        new_row = [random.randint(0,9) for _ in range(len(main_matrix[0]))]
        new_matrix = main_matrix + [new_row]
        for row in new_matrix:
            print(row)

    elif choice == "2":
        new_matrix = [row + [random.randint(0,9)] for row in main_matrix]
        for row in new_matrix:
            print(row)

    elif choice == "3":
        


