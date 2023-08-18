string= input("Enter a string: ")
rev_string = string[::-1]
unique_chars = []
for char in rev_string:
    if char not in unique_chars:
        unique_chars.append(char)
print("Output reversed and removed duplicates:")
for i in unique_chars:
    print(i,end=" ")
