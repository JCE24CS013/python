A = int(input("Enter the first number A: "))
B = int(input("Enter the second number B: "))

print("Menu Driven Calculator")

def add(A, B):
    print("Sum is", A + B)

def subtract(A, B):
    print("Subtraction is", A - B)

def multiply(A, B):
    print("Multiplication is", A * B)

def division(A, B):
    print("Division is", A / B)
    

print("\t1. Addition")
print("\t2. Subtraction")
print("\t3. Multiplication")
print("\t4. Division")

ch = int(input("Enter your choice (1,2,3,4): "))

if ch == 1:
    add(A, B)

elif ch == 2:
    subtract(A, B)

elif ch == 3:
    multiply(A, B)

elif ch == 4:
    division(A, B)

else:
    print("Enter the correct choice")

