def get_integer(prompt):
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid integer.")

num = get_integer("Enter a number: ")
print("You entered:", num)