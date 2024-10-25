# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(user_input):

    new_sentence = ""
    #    Add your logic here
    new_sentence = new_sentence + user_input[0]


    for i in range(1, len(user_input)):
        char = user_input[i]

        if char.isupper():
            char = char.lower()
            new_sentence = new_sentence + ' '

        new_sentence = new_sentence + char

    return new_sentence.strip()

# Example usage

sentence = input("Please insert a phrase in \"XxxxXxxxXxx\" format: ")

#sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)