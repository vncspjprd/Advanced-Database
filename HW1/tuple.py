rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

temp_list = []
for i in range(rows):
    print(f"Row {i+1}")
    inner = []
    for j in range(cols):
        num = float(input(f"Enter number{j+1}: "))
        inner.append(num)
    temp_list.append(tuple(inner))
nested_tuple = tuple(temp_list)

print("\nThe numbers are:\n")
for inner in nested_tuple:
    print(" ".join(str(n) for n in inner))

search_num = float(input("\nSearch: "))

found_positions = []
for i, inner in enumerate(nested_tuple):
    for j, num in enumerate(inner):
        if num == search_num:
            found_positions.append((i, j))

if found_positions:
    positions_str = " and ".join([f"Row {pos[0]}, Col {pos[1]}" for pos in found_positions])
    print(f"\nNumber {search_num} found at {positions_str}.")