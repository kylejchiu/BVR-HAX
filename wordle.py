import random

all_words = ["about", "above", "after", "again", "ahead", "alert", "allow", "amber", "anger", "angle", "angry", "array", "asset", "audio", "award", "aware", "beach", "beast", "begin", "belly", "below", "bench", "berry", "blaze", "block", "blood", "board", "bonus", "booth", "broke", "brush", "candy", "cause", "check", "chess", "chief", "clean", "clear", "clock", "close", "coach", "color", "count", "craft", "cross", "dance", "death", "devil", "drink", "drill", "drive", "drown", "enter", "event", "exact", "fancy", "favor", "fever", "field", "first", "fixer", "flame", "floor", "focus", "found", "fresh", "group", "heart", "hotel", "house", "image", "index", "inner", "input", "jelly", "joint", "judge", "lemon", "level", "light", "local", "mango", "match", "money", "night", "noble", "noise", "ocean", "order", "other", "panel", "place", "plane", "power", "quick", "right", "round", "stone", "water", "worse"]

def get_feedback(guess, word):
    feedback = ""
    for i in range(5):
        if guess[i] == word[i]:
            feedback += "G"
        elif guess[i] in word:
            feedback += "Y"
        else:
            feedback += "_"
    return feedback

def play_wordle():
    word = all_words[random.randint(0, 99)]
    attempts = 6
    
    print("Welcome to Wordle!")
    
    while attempts > 0:
        guess = input("Enter a 5-letter word: ")
        
        feedback = get_feedback(guess, word)
        print("Feedback: " + feedback)
        
        if guess == word:
            print("Congratulations! You guessed the word.")
            break
        
        attempts -= 1
        stringattempts = str(attempts)
        print("Attempts left: " + stringattempts)
    
    print("Game over! The word was: " + word)

play_wordle()