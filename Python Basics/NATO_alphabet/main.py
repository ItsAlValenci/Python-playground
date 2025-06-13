
import pandas

file = "nato_phonetic_alphabet.csv"

alphabet = pandas.read_csv(file)
phonetic_dict = {row["letter"]:row["code"] for (index,row) in alphabet.iterrows()}
# phonetic_dict = {row.letter:row.code for (index,row) in alphabet.iterrows()} <--same result
# print (phonetic_dict)

def phonetic_generator():
    is_on = True

    while is_on:
        word = input("\nWhat do you want to say?: ").upper()
        try:
            result = [phonetic_dict[letter] for letter in word]

        except KeyError:
            print("Sorry, only letter allowed! ")
        
        else:
            print(result)
            print("")
            is_on = False


phonetic_generator()
