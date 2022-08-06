# if 3 > 5:
#     print("its right")
#
# else:
#     print("it`s wrong!")
# print("Done")

###### Тернарный оператор

# operand = 3
# result = operand ** 0.5 if operand >=3 else operand ** 2
#
# print(f"{result=}")
#
# ######### Работа над ошибками

# divider = 1
# try:
#     result = 1 / divider
#     result_1 = 4 ** 2
#     print("it`s OK")
# except:
#     print("It`s broken, sorry...")
#     result = 13
#
# print(result_1)

# divider = "sansa"
# try:
#     result = 1 / divider
#
# except ZeroDivisionError:
#     print("You can`t dividing on Zero")
#
# except:
#     print("it`s to hard for me")
#
# else:
#     print(f"Easy-peasy, {result=}")
#
# finally:
#     print("Done")

try:
    result = 1 / 0

finally:
    print("Done")

