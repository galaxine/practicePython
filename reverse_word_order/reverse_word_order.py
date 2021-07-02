from operator import indexOf


words = input("Enter a sentence in here for a moment\n")
split_string = words.split(" ")
split_string.reverse()
new_string = " ".join(split_string)
print(new_string)