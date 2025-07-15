# Count to n and print each number
n = int(input("Enter the value of n: "))

def count_to_n(x = n):
    for i in range(1, x + 1):
        print(1, end=' ')
    print()

print(f"Going to count to {n} . . .")
count_to_n(n)
# ----------------
print("First modification to 2nd commit.")
print("Added for testing commits and pushes.")