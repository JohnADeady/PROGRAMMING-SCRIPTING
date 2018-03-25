# John Deady, 2018-23-02
# Mad Libs Generator

# Adapted  from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# The program will first prompt the user for a series of inputs a la Mad Libs.
#Then, once all the information has been inputted, the program will take that data and place them into a premade story template. 
# You’ll need prompts for user input, and to then print out the full story at the end with the input included.
# To find a solution to this problem I used Stackflow.

Print ("welcome to Mad Libs")                           # Inspired by Summer Son’s Mad Libs project with Javascript

adjective = input("Please input an adjective:")         # You will be prompted to input an adjective
noun = input ("Please input a noun:")                   # You will be prompted to input a noun
animal = input("Please input an animal:")               # You will be prompted to input a animal
noise = input ("Please input a noise:")                 # You will be prompted to input a noise

print(adjective, "Macdougal", "had", "a", noun, noise)  # This will print out a line with your inputs
