##### 1 #####

username = input("Please tell me your name (use only letters and spaces)")
result = f"{username}"
print("username-->", result)

##### 2 #####

username_without_spaces = result.strip()
print("username_without_spaces-->", username_without_spaces)

####3####
username_first_capital = username_without_spaces.capitalize()
user_welcome = f"Hello {username_first_capital}, I am glad to see you!"
print(user_welcome)

####4####
print("number of letters in username -->", len(username_without_spaces))

####5####
print("username backwards -->", result[::-1])