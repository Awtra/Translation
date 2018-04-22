#Ali Mody
#This program is used to translate an English word to Pig Latin.

#Initialize the Variable.
word = ""

# This loop takes the inputted word and uses the print statement
# to show you what the Pig Latin version of that word is.

while word != "Enter":
    word = input("Please enter a word that you would like to be translated:  ")
print(word[1:] + word[0] + "ay")
