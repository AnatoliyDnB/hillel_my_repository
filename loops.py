some_symbols = input("Hey you! Write everything what you want=) :")
certain_symbols = f"{some_symbols}"
print(certain_symbols, type(certain_symbols))

#####I fuckING hate this SHIT!
for letter in certain_symbols:

    if letter in "ABCDEFGQWRTYUIOPLKJHSZXVNM":
        print(letter)
        continue

    elif letter in "aAeEyYiIoO":
        print(letter)
        continue

    # collector_letters = ""
    # for index, element in enumerate(certain_symbols):
    #
    #     collector_letters += element
    #     if element in " ":
    #         print(f"{index=}|{element=}")


print("fucking nice")