symbol_1 = input("Please, enter the first digit")
number_1 = f"{symbol_1}"
print(number_1, type(number_1))     # len(number_1)

symbol_3 = input("Please, enter math sign which "
                 "you want to use (+ , - , * , / , ** )")
sign = f"{symbol_3}"
print(sign)

sign = "+"

try:
    sign = "+"

except:
    sign = "-"

except:
    sign = "*"

except:
    sign = "/"

except:
    sign = "**"

else:
    print("Sorry, but this sign is invalid")

finally:
    print("Done")

symbol_2 = input("Please, enter the second digit")
number_2 = f"{symbol_2}"
print(number_2, type(number_2))     # len(number_2)

try:
    sign = "+"
    print(int(number_1) + int(number_2))
except:
    sign = "-"
    print(int(number_1) - int(number_2))

except:
    sign = "*"
    print(int(number_1) * int(number_2))

except:
    sign = "/"
    print(int(number_1) / int(number_2))

except:
    sign = "**"
    print(int(number_1) ** int(number_2))

else:
    print("Sorry, but this sign is invalid")

finally:
    print("Done")