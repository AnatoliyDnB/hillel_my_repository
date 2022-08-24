while True:
    symbol_1 = input("Please, enter the first digit")
    number_1 = f"{symbol_1}"
    if number_1 == "exit":
        print("Breaking cycle!!!")
        break

    number_1 = float(number_1) if number_1.find(".") != -1 else int(number_1)
    print(number_1, type(number_1))

    symbol_2 = input("Please, enter the second digit")
    number_2 = f"{symbol_2}"
    if number_2 == "exit":
        print("Breaking cycle!!!")
        break

    number_2 = float(number_2) if number_2.find(".") != -1 else int(number_2)
    print(number_2, type(number_2))

    symbol_3 = input("Please, enter math sign which "
                     "you want to use (+ , - , * , / , ** )")
    sign = f"{symbol_3}"
    if sign == "exit":
        print("Breaking cycle!!!")
        break

    match sign:

        case "+":
            int_result = number_1 + number_2  # int-result - is intermediate result

        case "-":
            int_result = number_1 - number_2

        case "*":
            int_result = number_1 * number_2

        case "/":
            try:
                number_2 != 0
                int_result = number_1 / number_2

            except ZeroDivisionError:
                print("You can't dividing on zero")

        case "**":
            int_result = number_1 ** number_2

        case _:
            print("Sorry, but your math sign is invalid")

    if type(number_1) == float or type(number_2) == float:
        result = float(int_result)
        print("result=", result, type(result))

    else:
        result = int(int_result)
        print("result=", result, type(result))

    ###################### TASK №5.2 ########################
    num_1 = str(number_1)
    print("orders of the first number =", len(num_1))

    num_2 = str(number_2)
    print("orders of the second number =", len(num_2))

    ###################### TASK №5.3 ########################
    if f"{number_1}" > f"{number_2}":
        print(f"{number_1}", ">", f"{number_2}")

    elif f"{number_1}" < f"{number_2}":
        print(f"{number_1}", "<", f"{number_2}")

    else:
        print(f"{number_1}", "=", f"{number_2}")
