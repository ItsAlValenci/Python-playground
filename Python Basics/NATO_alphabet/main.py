
import pandas
file = "nato_phonetic_alphabet.csv"

alphabet = pandas.read_csv(file)

phonetic_dict = {row["letter"]:row["code"] for (index,row) in alphabet.iterrows()}
# phonetic_dict = {row.letter:row.code for (index,row) in alphabet.iterrows()} <--same result
# print (phonetic_dict)

word = input("What do you want to say?: ").upper()
result = [phonetic_dict[letter] for letter in word]

print(result)

# print(alphabet)
