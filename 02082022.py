if 3 > 5:  # let's check these options 3 < 5, bool(True), "not empty"
    print("if block done")

else:
    print("else block done")

print("Done")

variable = "initial value"

condition = bool(3+4)
another_condition = bool(3-3)
another_condition_2 = 3 > 5
############################################################################################
value = 10

if value > 10 and 1 == 1:
    value **= 2

elif value > 4 or False:
    pass

elif value > (6-1):
    value -= 1

else:
    value /= 3

print(f"{value=}")
###########################################################################################

result = int(15/2)
if result == 7:
    print("usual case")


if (result := int(15/2)) == 7:
    print("walrus is cool")
###########################################################################################

operand = 3
result = operand ** 0.5 if operand >= 3 else operand ** 2  # if true_action if condition else false_action

print(f"{result=}")
###########################################################################################
response_code = 200  # status_code = requests.get("google.com").status

match response_code:
    case 500:
        print("Internal Server Error")
    case 200:                # RAW 200 == response_code
        print("OK")
    case 200:                # missed
        print("OK 2")
    case _:  # default case is recommended == RAW else-block form if-else condition
        print("Default case for all other results")
############################################################################################
etalon_code = 200   # try change to other
response_code = 100

match response_code:
    case 200 if response_code == etalon_code:
        print("OK")

    case 200:
        print("OK without response_code == etalon_code")

    case 500:
        print("Internal Server Error")

    case 418:
        print("I'm a teapot")

    case 300 | 301 | 302:
        print("Some 300th responses")

    case _:
        print("Default case for all other results")
###########################################################################################
divider = 0
try:
    result = 1 / divider  # was broken
    # result_1 = 4**2  # will be error

except:
    # pass
    # print("It's broken, sorry...")
    result = 13
    # print(result_1)  # will be error

print(result)
############################################################################################
try:
    result = 1 / 1

except:
    print("It's too hard for me")

else:  # only if try correct
    print(f"Easy peasy, {result=}")
###########################################################################################
try:
    # 1 run as is
    # 2 uncomment divider
    # 3 let's check these options for divider "10.0", int("10.0"), float("10.0")
    # divider = 0
    result = 1 / divider

except ZeroDivisionError:
    print("You can't dividing on zero")

except NameError:
    print("Unknown variable")

except (TypeError, ValueError):
    print("You make me sad")

except Exception as error:
    print(f"Unxpectable error - {error}")

else:
    print(f"Easy peasy, {result=}")
###########################################################################################
try:
    result = 1 / 0

except ZeroDivisionError:
    print("It's too hard for me")

except:
    print("It's too hard for me")
######################################################
else:  # "try" and "else"
    print(f"Easy peasy, {result=}")  # except doesn't

finally:
    print("Done")
###########################################################################################
try:
    result = 1 / 0

finally:
    print("Done")
###########################################################################################
number = int(input("Give me the number: "))

if number < 0:
    result = number * -1

elif 0 < number < 3:
    result = number ** 0.5

else:
    result = number * 2 if number < 100 else number % 100

    try:
        result = 100 / result

        if result % 2 == 1:
            result += 1

        match result:
            case 10 | 15 | 20:
                result /= 2

            case _:
                pass

    except ZeroDivisionError:
        print("You have no power here")

print(result)
