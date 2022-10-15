# Speedle
#### Video Demo:  https://youtu.be/ES09GRCexJE
#### Description: A spinoff of the popular online game Wordle. Rather than competing based on the number of words it takes to guess correctly, Speedle users compete on the time they take to guess said word.

## app.py
In app.py we have the backend to the Speedle using a flask application. There are two routes, index and game, defined in the code. In the index route, the games landing page is loaded. The game route allows for both GET (showing the user's average score) and POST (updating the user's average score) requests. User info is cached allowing players to know how their current score compares with their average score.

## speedle.db
speedle.db contains the user's game data. In the file, there is only one table with columns for the user's id (cached on the user's computer), the user's average score, and the number of games played. A weighted average formula is used in app.py to allow for an accurate average score. Additionally, the average score is stored in a float that stores five decimal places.

## requirements.txt
This file contains all the necessary libraries to run the app.

## word.txt
word.txt contains the list of words used in Speedle in proper formatting.

## templates
Templates comprise three html files: layout.html, index.html, and game.html.
- layout.html
In layout.html lies the reference of the bootstrap and jquery libraries that are needed for the CSS and javascript.
- index.html
index.html has only one javascript function which loads game.html when the play button is pressed. Also in index.html is a link to the original Wordle website. Originally, there was supposed to be more on the landing page, but it felt like the design became too cluttered and distracting. Additionally, Wordle does not have a landing page, thus a more complex design was ruled against.
- game.html
game.html contains a number of javascript functions to do the mechanics of the game. In the code, there is another list of all of the playable words. The determineWord() function randomly selects a new word from the list every time the game is replayed. The words are represented as a 2d array with rows representing each word and columns representing each letter within a word. I added a timer and made the words four letters to differentiate Speedle from Wordle. Just like Wordle, a bootstrap modal appears showing your previous scores after guessing the right word.

## static
The static folder consists of the leaderboard and settings icons in the navbar (they have no functionality, they are just for looks) and the CSS for the page.
