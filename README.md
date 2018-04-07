# Programming and Scritping Module 

This repository contains assignments for semster one of Data Analytics from GMIT. There are a total of 11 scripts where I will go into more detail below. The main purpose of these assignments is to understand and write programs using the [Python](https://www.python.org/) programming language. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms (ref [Python Tutorial](https://docs.python.org/3/tutorial/))

## Getting Starting
[Python](https://www.python.org/) is receommended to run these programs. In order to get started we must download [Anaconda](https://www.anaconda.com/download/) and then [VS Code](https://code.visualstudio.com/).

[Anaconda](https://www.anaconda.com/download/) is a free and open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment.

[VS Code](https://code.visualstudio.com/). is a source code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. (ref Wikipedia)

#### Installing Downloads
Step by sted guide for downloading [Anaconda](https://www.anaconda.com/download/):
1. Open Anaconda Download
2. Click Python 3.6 version
3. Follow the instructions on screen - unsure about settings accept the default settings.
4. Once completed test installation

Step by sted guide for downloading [VS Code](https://code.visualstudio.com/)
1. Open VS Studio Download
2. Depending on your OS system - click the appropriate one ie Windows, Mac.
3. Follow the instructions on screen - unsure about settings accept the default settings.
4. Once completed run a simple program 

Once these programs have been downloaded, we can now start running each script on [VS Code](https://code.visualstudio.com/). Copy and paste each script from [Github](https://github.com/JohnADeady/PROGRAMMING-SCRIPTING) and follow the instructions for each assigment.

## Assignment One (Week 1: 22-01-2018 to 28-01-2018)
Calculates the nth Fibonacci number.Fibonacci series is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.(ref Wikipedia). Change the program to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. Take A as the number 1, B as 2, C as 3, and so on. For example, my name is John, so I should calculate the 24th Fibonacci number because J is 8 and n is 14, giving 24 in total. 


## Assignment Two (Week 2: 29-01-2018 to 04-02-2018)
Calculates the nth Fibonacci number.Fibonacci series is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.(ref Wikipedia). Change the string variable to contain your own surname, and rerun it


## Assignment Three (Week 3: 05-02-2018 to 11-02-2018)
The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1 (ref Wikipedia).

A single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. The program will ask the user for the integer instead of specifying a value at the start of your code. 


## Assignment Four (Week 5: 19-02-2018 to 25-02-2018)
It is [Problem 5](https://projecteuler.net/problem=5) from Project Euler. The problem is as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. Add your answer to your GitHub repository.


## Assignment Five (Week 6; 26-02-2018 to 04-03-2018)
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.(ref Wikipedia)

Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.


## Assignment Six (Week 7: 05-03-2018 to 11-03-2018)
A Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the function by calling it with the values 5, 7, and 10.


## Extra Assignments
#### Euler Problem 1
[Problem 1](https://projecteuler.net/problem=1) If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

#### Euler Problem 3
[Problem 3](https://projecteuler.net/problem=3) The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143?

#### Euler Problem 6
[Problem 6](https://projecteuler.net/problem=6) The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)2 = 552 = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#### Dice Rolling Simulator 
[Dice Rolling Simulator](https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/) program involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.

#### Guess the Number
[Guess](https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/). The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.

#### Mad Libs Generator
[Mad](https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/) program will first prompt the user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then, once all the information has been inputted, the program will take that data and place them into a premade story template. You’ll need prompts for user input, and to then print out the full story at the end with the input included.


## Built With
This repository contains Python code only.

## Licence
This project is licensed under the Apache License 2.0

## Acknowledgements
 - Thanks to the users of stackflow for their assistance
