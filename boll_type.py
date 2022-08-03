##### 1 #####
print("\n TASK №1")

comparison_result_1 = 3 < 5
print("3 < 5 is", comparison_result_1)

comparison_result_2 = 3 <= 5
print("3 <= 5 is", comparison_result_2)

comparison_result_3 = 3 != 5
print("3 != 5 is", comparison_result_3)

##### 2 #####
print("\n TASK №2")

right_result_1 = 5 == 5
print("5 = 5 is", right_result_1)

right_result_2 = 5 >= 5
print("5 >= 5 is", right_result_2)

right_result_3 = 5 <= 5
print("5 <= 5 is", right_result_3)

##### 3 #####
print("\n TASK №3")
combination_1 = True and (True or False)
print(f"{combination_1 = }")

combination_2 = True or (True and False)
print(f"{combination_2 = }")

combination_3 = True or (True or False)
print(f"{combination_3 = }")

combination_4 = True and (True and not False)
print(f"{combination_4 = }")

combination_5 = (not True or True) or False
print(f"{combination_5 = }")

##### 4 #####
print("\n TASK №4")

bool_none = bool(None)
print(f"{bool_none = }")

bool_digit_1 = bool(7)
print(f"{bool_digit_1 = }")

comparison_result_1: bool = bool_none == bool_digit_1
print("bool_none == bool_digit_1= ", comparison_result_1)

comparison_result_2: bool = bool_none >= bool_digit_1
print("bool_none >= bool_digit_1= ", comparison_result_2)

comparison_result_3: bool = bool_none > bool_digit_1
print("bool_none > bool_digit_1= ", comparison_result_3)

comparison_result_4: bool = bool_none != bool_digit_1
print("bool_none != bool_digit_1= ", comparison_result_4)

comparison_result_5: bool = bool_none <= bool_digit_1
print("bool_none <= bool_digit_1= ", comparison_result_5)

comparison_result_6: bool = bool_none < bool_digit_1
print("bool_none < bool_digit_1= ", comparison_result_6)

one_space_str = bool(" ")
print(f"{one_space_str = }")

bool_digit_2 = bool(10-1)
print(f"{bool_digit_2 = }")

second_comparison_result_1: bool = one_space_str == bool_digit_2
print("one_space_str == bool_digit_2= ", second_comparison_result_1)

print("\n FULL VERSION OF SECOND COMPARISON:")

second_comparison_result_2 = one_space_str != bool_digit_2
print("one_space_str != bool_digit_2= ", second_comparison_result_2)

second_comparison_result_3 = one_space_str >= bool_digit_2
print("one_space_str >= bool_digit_2= ", second_comparison_result_3)

second_comparison_result_4 = one_space_str > bool_digit_2
print("one_space_str > bool_digit_2= ", second_comparison_result_4)

second_comparison_result_5 = one_space_str <= bool_digit_2
print("one_space_str <= bool_digit_2= ", second_comparison_result_5)

second_comparison_result_6 = one_space_str < bool_digit_2
print("one_space_str <= bool_digit_2= ", second_comparison_result_6)