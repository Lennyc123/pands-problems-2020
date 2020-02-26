# The following program reads in a text file
# and outputs the number of "e's" it contains.

filename = input("Enter file name: ") # User is prompted to input the name of a .txt file
l = str("e") # The program is told which letter to look for i.e "e"
k = 0 # used as a place holder for number of e's
 
with open(filename, 'r') as f: # The provided .txt file is opened in read mode.
    for line in f: # Usage of for loop to read through each line in the file
        words = line.split() # Each line is split into a list of words using split()
        for i in words: # Used to traverse through the words list
            for letter in i: # Used to traverse through the letters in the word
                if(letter==l):
                    k=k+1 # Addition of "e" to the number of "e's" - if another instance of "e" is found
print("Your text file contains this many e's:") # string for user interaction
print(k) # Number of e's within the .txt file is printed

#references
# https://docs.python.org/3/tutorial/inputoutput.html
# https://www.computerhope.com/issues/ch001721.htm
# https://www.sanfoundry.com/python-program-read-file-counts-number/