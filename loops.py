some_symbols = input("Hey you! Write everything what you want=) :")

upper_letters = ""
index_of_spaces = ""
vowels_letters = ""
counter = 0

for index, letter in enumerate(some_symbols):
    if letter.isspace():
        index_of_spaces += str(index) + ","

    if letter.isupper():
        upper_letters += letter

    if letter in "aeiouyAEIOUY":
        vowels_letters += letter

    if letter.isdigit:
        counter += 1
        if counter == 3:
            result = "Breaking cycle!!! Three digit sequence found"
            break
    if not letter.isdigit():
        counter = 0
        continue
else:
    result = "The cycle is complete"

print(f"{upper_letters=}")
print(f"{index_of_spaces=}")
print(f"{vowels_letters=}")
print(result)
