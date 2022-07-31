username = input("Please tell me your name")
result = f"Hello {username}, I am glad to see you!"
print(result)

fav_number = input("Please enter your favorite fractional number")
float_number = float(f"{fav_number}")  #we took whole float number
print(float_number)

int_number = int(float_number)
print(int_number)

exponential_number = int_number ** 4
print(exponential_number)

square_root = int_number ** 0.5
print(square_root)

division_remainder = int_number % 2
print(division_remainder)


# ============================= FULL VERSION ============================
#
# username = input("Please tell me your name")
# result = f"Hello {username}, I am glad to see you!"
# print(result)
#
# fav_number = input("Please enter your favorite fractional number")
# float_number = float(f"{fav_number}")  #we took whole float number
# print("Float number", float_number, type(float_number))
#
# int_number = int(float_number)
# print("Integer number = ", int_number, type(int_number))
#
# exponential_number = int_number ** 4
# print("Exponentiation 4 = ", exponential_number, type(exponential_number))
#
# square_root = int_number ** 0.5
# print("Square root from 2 = ", square_root, type(square_root))
#
# division_remainder = int_number % 2
# print("Remainder of division by 2 = ", division_remainder, type(division_remainder))