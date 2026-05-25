num = input("Enter the number to check palindrome: ")

def palindrome(num):
    if num == num[::-1]:
        return True
        return False

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")