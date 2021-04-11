# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.




while(True): 
    user_typed = input("sup cutie, enter a word or phrase: ")
    print(user_typed)

    word_length = len(user_typed) - user_typed.count(" ")
    print(f'what you entered is {word_length} characters long')

    if user_typed == 'quit': 
        break















#while loop is a float chart

# while(true): 
#     user_types = input('attend class?')
#     if (user_types) == 'no'
#         print(":( guess I'll sleep :(")
#         break
#     elif user_types == "yes":
#         print("yay, its time for class")
#     else: 
#         print('you typed something that was not a yes or no') 
