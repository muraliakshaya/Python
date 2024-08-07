import random

words=["python", "java", "kotlin", "javascript", "swift", "ruby"]

#choose random word from list
chosen_word=random.choice(words)
word_display=['_' for _ in chosen_word]
attempts=8

print(f"Welcome to the Hangman game, you have {attempts} attempts to guess the word.")

while attempts > 0 and '_' in word_display:
    print("\n" +''.join(word_display))
    guess= input("Guess a letter: ").lower()
    #if guessed letter in chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index]=guess
    else:
        print("Letter not in word, try again!")
        attempts-=1
        
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")