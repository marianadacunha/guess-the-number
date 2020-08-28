# Guess the number

This is a game that uses random numbers, loops and inputs from the user in a short program.

In this game, the for loop runs until the number guessed by the user is equal to the random generated number or until the number of attempts is less than the maximum number of given chances. If the number of attempts becomes greater than the number of chances, the game stops and the user loses the game. If the user guesses the correct number in the given number of chances, then he will win. After every guess made by the user, the program informs whether the guessed number was smaller or greater than the actual generated number. In this code, the random number is generated between 1-100 using the randint() function.

# Rules

1. The computer will choose any random number between 1 to 100. Then you will try to guess this secret number;
2. If you fail to enter the random number chosen by the computer, then you will get a hint. The hints will be like these:
  * Your guess was low;
  * Your guess was high;
3. With the help of these hints, you will have to find the random number chosen by the computer.
