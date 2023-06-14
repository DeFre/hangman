import random

class hangman:
    """
    Class that defines everything we need for our game
    """
    pass

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']         #the list of words the game can choose from
        self.chosen_word = random.choice(self.possible_words) #so that it can be displayed in game_over
        self.word_to_find = list(self.chosen_word)        #a list containing all the letters of the word which need to be guessed as strings
        self.lives = 5      #the number of lives a player still has left
        self.correctly_guessed_letters =  ["_" for i in range (len(self.word_to_find))]         #a list of strings where each element will be a letter guessed by the user. At the start, it should be equal to: `_ _ _ _ _`, with the same number of `_` as the length of the word to find.
        self.wrongly_guessed_letters =  []      #a list of strings where each element will be a letter guessed by the user that is not in the `word_to_find`
        self.turn_count = 0         #the number of turns played by the player represented as an `int`.
        self.error_count = 0        #the number of errors made by the player

    def play(self):
        """
        This method manages each turn: asks for an input, checks the word and adds new letters, takes lives where necessary
        """
        guess = input("Please type a letter:").lower()
        self.turn_count += 1
        if guess in self.word_to_find:
            indices = [i for i, x in enumerate(self.word_to_find) if x == guess]
            for i in range(len(indices)):
                self.correctly_guessed_letters[indices[i]] = guess
        else:
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
        
                
    def start_game(self):
        """initiates the game"""
        print("Can you guess this word? ", self.correctly_guessed_letters)

        while self.lives > 0:
            if self.correctly_guessed_letters != self.word_to_find:    
                self.play()
                print(self.correctly_guessed_letters)
                print("It's not one of these letters:", self.wrongly_guessed_letters)
                print("You have been playing for ", self.turn_count, " turns.")
                print("You have ",self.lives, " lives left")
            else:
                self.well_played()
                return
        self.game_over()
        
    
    def game_over(self):
        """Displays GAME OVER and the word you were looking for"""
        print("GAME OVER")
        print("The word you were looking for was ", self.chosen_word)
        return

    def well_played(self):
        """Displays GAME OVER and the word you were looking for"""
        print(self.correctly_guessed_letters)
        print("you made ", 5-self.lives, " mistakes, but you made it!")
        print("Well Played!")
        

