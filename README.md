# Guess the number game.

### guess_the_number_v1:

This is a simple console game 'guess the number'. The computer draws a number in the range of 1 &ndash; 100. Then:


1. Ask for: 'Guess the number: ' and get the number from the keyboard.
2. It will be checked if the entered string is really a number and in case of an error it will display a message 'It's not a number!', 
and then return to point 1.
3. If the user entered number is less than the drawn number, a message 'To small!' will be displayed, 
and then return to point 1.
4. If the user entered number is greater than the drawn number, a message 'To big!' will be displayed, 
and then return to point 1.
5. If the number given by the user is equal to the drawn number, the message 'You win!' will be displayed,
and the program is terminated.

##### Example:
```plaintext
Guess the number: Hi,
It's not a number!
Guess the number: 7
To small!
Guess the number: 80
To big!
Guess the number: 29
You win!
```

### guess_the_number_v2:

The opposite situation than in the program 'guess_the_number_v1'. 
The user draws a number in range 1 &ndash; 1000 and the computer makes a guesswork. 
It will do this in a maximum of 10 tries. 

The player's task is to answer 'To small', 'To big', 'You win'.


### guess_the_number_v3:

This is 'guess_the_number_v2' implemented in a web application using the Flask framework.
A form with three buttons: **To small**, **To big**, **You win** is displayed to the user. 


