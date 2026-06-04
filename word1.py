l = []
no = int(input("Enter the number of words: "))
for i in range(no):
    word = input("Enter a word: ")
    l.append(word)
with open("word.txt", "w+") as f:
    for word in l:
        f.write(word + "\n")
    words = f.read()
    print("Contents in uppercase:")
    for line in words.splitlines():
        print(line.upper())
