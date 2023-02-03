'''
Homework 1
Name: Zachary Pace
Date: 2/2/2023
Description: faulty Security questions split into 3 parts

   Part 1 - Dynamic Math Problems
        Solve dynamically generated math questions
   Part 2 - Arbitrary Security Questions
        Basically just input words till you get the correct character count
   Part 3 - Remainder Guess letter
        Guess a pseudo-random letter from your name

    Admittedly this is tedious to do properly so if you put your name as 'Cheater'
you can go through it pretty easily
'''

import random

top_sneaky_number = 42
locked = True

while locked:
    locked = False
    user_name = str(input("What is your name?"))

# Part 1 - Dynamic Math Problems

    print("\n\tPart 1 - Dynamic Math Problems\nSolve the following 3 Questions\n")
    for i in range(3):
        # generate 3 random numbers and add an unknown
        num_list = [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5), "?"]
        # shuffle the position of the unknown
        random.shuffle(num_list)
        print(str(i + 1)
              + "/3) (" + str(num_list[0])
              + ") + (" + str(num_list[1])
              + ") - (" + str(num_list[2])
              + ") = " + str(num_list[3]))
        unknown_index = num_list.index("?")

        # Check if it's a cheater and skip questions
        if user_name == "Cheater":
            print("Cheater...")
            continue
        else:
            num_list[unknown_index] = int(input("What is the Solution?"))

        if (num_list[0] + num_list[1]) - (num_list[2] + num_list[3]) == 0:
            print("Correct!")
        else:
            print("Incorrect")
            locked = True
            break

    # one answer was incorrect so restart
    if locked:
        continue

# Part 2 - Arbitrary Security Questions

    print("\n\tPart 2 - Arbitrary Security Questions\nAnswer the following Security Questions\n")
    user_input_length = 0
    target_word_length = random.randint(3, 6)
    i = 0
    # List of prompts that will be asked
    Questions = ("What is you're favorite food?", "What was you're Childhood nickname?", "What is you're pets name?")

    # We don't actually care about the answers, we just need the character length to match the target
    while user_input_length != target_word_length:
        # Checks for Cheater and give hint
        if user_name == "Cheater":
            print("The answer is any word with " + str(target_word_length) + " Characters")

        # Prints promts until we run out of Question then we just give it to them
        if i < len(Questions) - 1:
            user_input_length = len(str(input(Questions[i])))
        elif i == len(Questions) - 1:
            user_input_length = len(str(input(Questions[i] + " That's my last prompt...")))
        else:
            user_input_length = len(str(input("...I'm out of prompts. Just input a word with " + str(target_word_length)
                                          + " Characters")))
        i = i + 1

# Part 3 - Remainder Guess letter

    print("\n\tPart 3 - Remainder Guess letter\nI've picked a \'Random\' letter from your name, guess which one\n")
    # guess a letter in your name, but it's not truly random
    user_guess = "aa"
    # Pick the letter using % operator
    answer = user_name[1000 % (len(user_name) - 1)]
    while answer != user_guess:
        # Checks for Cheaters and gives answer
        if user_name == "Cheater":
            print("The answer is " + str(answer))
        user_guess = str(input("Guess a Letter"))

# They made it out of the loop so print the secret number
print("\nThe Secret Number is: " + str(top_sneaky_number) + " the secret of the universe")