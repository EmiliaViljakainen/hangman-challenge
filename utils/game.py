import random


class Hangman:

    def __init__(self):
        self.possible_words: List[str] = ["becode", "learning", "mathematics", "sessions"]
        self.word_to_find: List[str] = random.choice(self.possible_words)
        self.word_to_find = list(self.word_to_find)
        #underscores as many than letters
        self.well_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        #how to detect the correct letter places (range loop?)?

        self.bad_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.lives: int = 5

        #turn_count attribute that contains the number of turns played by the player.


    def play(self):

        while True:
            letter = input(f"Enter one letter: ")
            if len(letter) == 1:
                if isalpha(letter):
                  break
                else:
                    print("It has to be letter.")
            else:
                print("Enter only one letter")

            self.turn_count += 1



            #Each time the player finds a correct letter,
            # replace the _ with the letter that the user suggested.

            # If the player guessed a letter well: add it to the
            # well_guessed_letters list

            self.well_guessed_letters += 1


        #else:
            #self.bad_guessed_letters.append(letter)
            #self.error_count += 1
            #self.lives -= 1


    #def game_over(self):

    #def well_played(self):

    #def start_game(self):
        #print("Lets play Hangman")


#h = Hangman()!!!!
#print(h.word_to_find)!!!

#ha = Hangman()
#print(ha.well_guessed_letters)
#  WOHOO ['_', '_', '_', '_', '_', '_']



