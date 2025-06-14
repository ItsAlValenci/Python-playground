import random
logo = ''' 
                                               _____                                                       
|         |       .'.       |..          |  .-~     ~.        .'. .`.             .'.       |..          | 
|_________|     .''```.     |  ``..      | :                .'   `   `.         .''```.     |  ``..      | 
|         |   .'       `.   |      ``..  | :     _____    .'           `.     .'       `.   |      ``..  | 
|         | .'           `. |          ``|  `-._____.'| .'               `. .'           `. |          ``| 
                                                                                                           
'''

#list of common english words
word_list = ['apple', 'banana', 'carrot', 'dog', 'elephant', 'fish', 'giraffe', 'house', 'ice', 'jump', 'key', 'love', 'money', 'nature', 'ocean', 'pizza', 'queen', 'rabbit', 'sun', 'tree', 'umbrella', 'violet', 'water', 'xylophone', 'yellow', 'zebra', 'air', 'ball', 'cat', 'door', 'egg', 'fire', 'guitar', 'hat', 'island', 'jacket', 'kite', 'lion', 'moon', 'night', 'oasis', 'peach', 'quilt', 'rain', 'sea', 'train', 'understand', 'van', 'waterfall', 'x-ray', 'you', 'zip', 'alien', 'book', 'chair', 'dolphin', 'earth', 'fishing', 'goat', 'home', 'internet', 'jungle', 'kitchen', 'lunch', 'music', 'newspaper', 'oasis', 'paint', 'question', 'rainbow', 'shoe', 'tiger', 'unicorn', 'violin', 'window', 'xmas', 'yacht', 'zoo', 'angel', 'building', 'camel', 'dance', 'eagle', 'flower', 'golf', 'hero', 'ice-cream', 'juice', 'kangaroo', 'laptop', 'mouse', 'noise', 'opinion', 'parrot', 'queen', 'road', 'soccer', 'teacher', 'umbrella', 'vacation', 'whale', 'xylophone', 'yoga', 'zipper']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
          '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
          '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
          '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
          '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
          '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
          '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

win = """
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
"""

lose = """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                  
"""


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
input("\n\nPress enter to start the game\n")

#Testing code and validation
#print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks spaces
display = []
used_words = []
for _ in range(word_length):
    display += "_"

#Start of the game
while not end_of_game:
    guess = input("\nGuess a letter: ").lower() #word in lower case
    used_words.append(guess)

    #For words you already guessed 
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            

    #turning the list into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You {win}.")
        
    print(stages[lives])
    print(used_words)

if lives == 0:
    print(f"\nYou are out of lives!!\nThe word was '{chosen_word}'")
    print(f"{lose}")

           