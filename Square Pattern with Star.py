n = int(input("Enter the number of rows: "))
for row in range(1, n+1):
    for col in range(1, n+1):
        print("*", end=" ")
    print()