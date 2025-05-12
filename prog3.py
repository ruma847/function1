def add(P, Q):
    return P + Q

def add(P, Q):
    return P - Q

def add(P, Q):
    return P * Q

def add(P, Q):
    return P / Q

print("Please select the operation.")
print("a. Add")
print("s. subtract")
print("m. multiply")
print("d. division")

choice = input("Pleae enter choice (a/ s/ m/ d):")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 's':
    print(num_1, "-", num_2, "=", add(num_1, num_2))
elif choice == 'm':
    print(num_1, "*", num_2, "=", add(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", add(num_1, num_2))