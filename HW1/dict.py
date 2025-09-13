
rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

numbers_dict = {}
for i in range(rows):
    print(f"Row {i+1}")
    for j in range(cols):
        num = float(input(f"Enter number{j+1}: "))
        numbers_dict[(i, j)] = num

print("\nThe numbers are:\n")
for i in range(rows):
    row_values = [str(numbers_dict[(i, j)]) for j in range(cols)]
    print(" ".join(row_values))

search_num = float(input("\nSearch: "))

found_positions = []
for key, value in numbers_dict.items():
    if value == search_num:
        found_positions.append(key)

if found_positions:
    positions_str = " and ".join([f"Row {pos[0]}, Col {pos[1]}" for pos in found_positions])
    print(f"\nNumber {search_num} found at {positions_str}.")
else:
    print(f"\nNumber {search_num} not found.")