nestedlist=[]
row=int(input("Enter row : "))
col=int(input("Enter col : "))
for x in range(row):
    print(f"Row {x+1}")
    innerlist=[]
    for y in range(col):
        score=float(input(f"Enter number {y+1}: "))
        innerlist.append(score)
    nestedlist.append(innerlist)

print("\nThe numbers are:")
for x in nestedlist:
    print(" ".join(str(i) for i in x))

search = float(input("\nSearch: "))
positions = []
for i in range(row):
    for j in range(col):
        if nestedlist[i][j] == search:
            positions.append(f"Row {i}, Col {j}")

if positions:
    print(f"\nNumber {search} found at " + " and ".join(positions))
else:
    print(f"\nNumber {search} not found.")