import random
from hangmanwords import word_list
from hangman_art import stages
from hangman_art import logo

#word_list = ['adavark','hangman','baboon','camel','right']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

print(logo)

#print(f"Psst, the solution is {chosen_word}")

display=[]
for letter in chosen_word: # or youcan also use for letter in range(len(chosen_word))
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"You've already gueesed {guess}")
    

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position : {position} \n Current letter: {letter}\n Guessed leter: {guess}")
        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        print(f"You've guessed {guess} that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
           end_of_game=True 
           print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")
    
    print(stages[lives])
