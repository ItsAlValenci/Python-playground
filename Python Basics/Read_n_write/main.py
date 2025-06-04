#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


input_template = "./Input/Letters/starting_letter.txt"
input_names = "./Input/Names/invited_names.txt"
outputs = "./Output/ReadyToSend"


# Long Version
# invite_names = []
# with open(input_names, mode= "r") as guest_list:
#     lines = guest_list.readlines()
#     for name in lines:
#         clean = name.strip()
#         invite_names.append(clean)

#simplified:
with open(input_names, mode="r") as guest_list:
        invite_names = [name.strip() for name in guest_list.readlines()]  # Remove declaring list and aditional newline


with open(input_template, mode= "r") as template:
    text = template.read()

for name in invite_names:
    personalized_letter = text.replace("[name]",name)
    export_path= f"{outputs}/letter_for_{name}.txt"
    with open (export_path, mode= "w") as  output_letter:
        output_letter.write(personalized_letter)

print("\n\nScript Done")