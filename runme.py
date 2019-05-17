#word guess game
#5/9/2019
#francis michael tayag

import random

word_list = [("towel", "a cloth used for drying oneself"),
             ("peace", "the abscence of violence"),
             ("galaxy", "a system of millions or billions of stars"),
             ("star", "a large celestial body that produces light"),
             ("ear", "an organ used for hearing"),
             ("dance", "a successive group of bodily motions usually executed to music"),
             ("earth", "the third planet from the Sun"),
             ("festival", "a celebration, marked by feasting, ceremonies, or other observances")
             ("flower", "the seed-bearing part of a plant"),
             ("tree", "a tall plant with a trunk and branches made of wood")]

running = True
score = 0
mistakes = 0
question_number = 1
rng = random.randint(0, len(word_list) - 1)

print("Welcome to Word Guess! Type 'exit' to exit the game. Type 'hint' for a hint on what the word is, but doing so will deduct your score!")
while running:
    print("\n")
    print(f"{question_number}. Guess the word! What is...{word_list[rng][1]}?")
    answer = input("Answer: ")
    answer = answer.lower()
    
    if answer == word_list[rng][0]:
        score += 1
        word_list.pop(rng)
        question_number += 1
        print("Correct answer!")
        print(f"Score: {score}\nMistakes: {mistakes}")
        if len(word_list) == 0:
            print("\n")
            print("Aww crumbs...looks like I'm out of questions! You win!")
            print(f"Thanks for playing! Your score was {score}, and you made {mistakes} mistakes.\nFINAL SCORE: {score - mistakes}")
            running = False
        else:
            rng = random.randint(0, len(word_list) - 1)
    elif answer == "exit" or answer == "\'exit\'":
        print(f"Thanks for playing! Your score was: {score}, and you made {mistakes} mistakes.\nFINAL SCORE: {score - mistakes}")
        running = False
    elif answer == "hint" or answer == "\'hint\'":
        hint_rng = random.randint(0, 3)
        if hint_rng == 0:
            score -= 1
            print(f"It is a {len(word_list[rng][0])} letter word!")
            print(f"Your score has been deducted! Score: {score}")
        elif hint_rng == 1:
            score -= 1
            print(f"It starts with the word '{word_list[rng][0][:1]}'!")
            print(f"Your score has been deducted! Score: {score}")
        elif hint_rng == 2:
            score -= 1
            print(f"It starts with the word '{word_list[rng][0][:1]}' and ends with the word '{word_list[rng][0][-1:]}'!")
            print(f"Your score has been deducted! Score: {score}")
        elif hint_rng == 3:
            print(f"It is a {len(word_list[rng][0])} letter word!")
            print("I'm feeling a little nice at the moment so I won't deduct your score.")
    else:
        mistakes += 1
        question_number += 1
        print(f"Wrong answer! The correct answer is: {word_list[rng][0]}")
        print(f"Score: {score}\nMistakes: {mistakes}")
        word_list.pop(rng)
        if len(word_list) == 0:
            print("\n")
            print("Aww crumbs...looks like I'm out of questions!")
            print(f"Thanks for playing! Your score was {score}, and you made {mistakes} mistakes.\nFINAL SCORE: {score - mistakes}")
            running = False
        else:
            rng = random.randint(0, len(word_list) - 1)
