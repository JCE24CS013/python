string = input("Enter the string: ")
def count_vowels(string):
    count = 0
    for i in string:
        if i in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            count += 1
    if count == 0:
        print("Vowels not found")
    else:
        print("Number of vowels is:", count)
count_vowels(string)