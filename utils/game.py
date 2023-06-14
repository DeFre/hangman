import random

class hangman:
    """
    Class that defines everything we need for our game
    """
    pass

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions'] #the list of words the game can choose from
        self.word_to_find = list(random.choice(self.possible_words))  #a list containing all the letters of the word which need to be guessed as strings
        self.lives = 5 #the number of lives a player still has left
        self.correctly_guessed_letters =  ["_" for i in range (len(self.word_to_find))] #a list of strings where each element will be a letter guessed by the user. At the start, it should be equal to: `_ _ _ _ _`, with the same number of `_` as the length of the word to find.
        self.wrongly_guessed_letters =  [] #a list of strings where each element will be a letter guessed by the user that is not in the `word_to_find`
        self.turn_count = 0 #the number of turns played by the player represented as an `int`.
        self.error_count = 0 #the number of errors made by the player

    def play(self):
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
        while self.lives > 0:
            self.play()
        self.game_over()
    
    def game_over(self):
        print("GAME OVER")


hang = hangman()
print(hang.word_to_find)
print(hang.correctly_guessed_letters)
print(hang.wrongly_guessed_letters)
hang.play()
print(hang.correctly_guessed_letters)
print(hang.wrongly_guessed_letters)
print(hang.turn_count)
print(hang.lives)



    