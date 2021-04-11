# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

user_entered = input("hey hottie, please enter a letter from the alphabet: ")
print(user_entered)

#here I take the letter entered and store it inside the variable 'question'

vowels = ['a', 'e', 'i', 'o', 'u']

# here I create an array that contains all the vowels which I can use 
# to compare with what the hottie entered in the 'question' variable 



for v in vowels: 
    if(v == user_entered):
        print('letter entered is a vowel')
        break
    else:
        print("letter entered is a consonant")


# now I am trying to create a loop with a condition inside that is 
# supposed to check for what the user enterred inside 'question' and then actually compare it with what is inside 
# the vowel array


# question = what the cx entered as the letter 
# 