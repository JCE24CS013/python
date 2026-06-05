def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Enter a non-zero number")
        return None

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = safe_divide(a, b)
print(result)