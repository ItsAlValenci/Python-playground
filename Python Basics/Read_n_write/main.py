# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# This will overwrite anything in the file or create a new one if do not exist 
with open("new_file.txt", mode="w") as file:
    file.write("New line of text weeeee!")

# This will append the new text to the existing one
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew line of text \nweeeee!")