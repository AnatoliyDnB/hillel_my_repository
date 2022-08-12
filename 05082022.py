# counter = 0
#
# while counter < 3:
#     counter += 2  # counter = counter + 2
#     print(f"One more iteration. {counter=}")
#     # here
#     print("still working")
#     counter -= 1  # counter = counter - 1
#
#
# print("Job is done")

# ####################################################
# my_string = ""
#
# while len(my_string := my_string + "@") < 4:  # len(my_string) < 4
#     print(f"inside loop {len(my_string)}")
#
#
# print(f"outside loop {len(my_string)}")
# ####################################################
# while True:
#     print("One more iteration of the infinite loop")  # Ctrl + C, to interrupt the program
#
# ####################################################
# counter = 0
#
# while counter < 5:
#     counter += 1
#
#     if counter == 3:
#         print("LOOK AT ME")
#         continue  # work with the nearest loop
#
#     print(f"One more iteration. {counter=}")
#
# print("Job is done")
# ####################################################
# counter = 0
#
# while counter < 100:
#     print("One more iteration")
#     counter += 1
#
#     if counter // 10 == 1:
#         print("Loop is breaking")
#         break   # work with the nearest loop
#     print(f"{counter=}")
#
# # print("Job is done")
# # ####################################################
# counter = 0
#
# while counter < 10:
#     print("One more iteration")
#     counter += 1
#     print(f"{counter=}")
#
#     if counter // 100 == 1:
#         print("Loop is breaking")
#         break
#
# else:
#     print("Block else")
#
# print("Job is done")
# ####################################################
# counter = 0
# counter_1 = 0
# counter_2 = 0
#
# while counter < 100:
#     print("One more iteration")
#     counter += 1
#
#     if counter // 10 == 1:
#         print("Loop is breaking")
#         break
#
# else:
#     print("Block else")
#
# print("Job is done")
# ####################################################
# counter = 0
#
# while counter < 10:
#     counter += 1
#     if counter // 10 == 1:
#
#         while True:
#             print("inner loop")
#             break
#
#     print("Last line of outer loop")
#
# for i in "abcd":  # simple sample
#     print(i)
#
#
# iterable_object = "loop it's easy"
# for letter in iterable_object:
#     print(letter)
#
# print("loop is finished")
# ####################################################
# iterable_object = "for-loop with break operator"
#
# for letter in iterable_object[:10]:
#     print(letter)
#
#     if letter in "abco":
#         print("loop break")
#         break
#
# print("loop is finished")
# ####################################################
# counter = 0
# iterable_object = "for-loop with break operator"
#
# for letter in iterable_object:
#     print(letter)
#     counter += 1
#
#     if counter == len(iterable_object) + 1:
#         print("counter achieved")
#         break
#
# else:
#     print("counter is not achieved")
#
# print("loop is finished")
# ####################################################
counter = 0
iterable_object = "for-loop with break operator"

for letter in iterable_object:
    print(letter)
    # counter += 1

    if counter == 3:
        print("counter achieved")
        break

else:
    print("counter is not achieved")

print("loop is finished")
# ####################################################
# for el in range(5):  # stop parameter
#     print(el)
#
# for el in range(2, 5):  # start and stop parameters
#     print(el)
#
# for el in range(1, 7, 2):  # start, stop and step parameters
#     print(el)
#
# for el in range(5, -5, -2):
#     print(el)
# ####################################################
object_for_enumerate = "for-loop with break operator"
collector_letters = ""

for index, element in enumerate(object_for_enumerate):
    print(f"{index=}|{element=}")

    collector_letters += element
    if len(collector_letters) == 6:
        break