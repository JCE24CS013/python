from datetime import date
message = input("Enter your message: ")
with open("diary.txt", "a") as file:
    file.write(str(date.today()) + " - " + message + "\n")
print("Saved")