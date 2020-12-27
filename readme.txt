Word Guess 
Version 2.0
by Zyenapz
	Website: zyenapz.github.io
	E-mail: zyenapz@gmail.com

Hey there, thanks for downloading this little game!
If you want to send feedback then send it at: zyenapz@gmail.com or you can comment about it on the GitHub page of the project :)

How to add new words?
This game is built to support the addition of new words very easily! Just follow these steps:

1. Go to the data folder and open words.py on your favorite text editor (such as Notepad)
2. To add a new word to a category, simply add the word and its definition in the words dictionary like so:
	{ WORD: DEFINITION }
3. To add a new category, simply do the following:
	words[CATEGORY] = { WORD: DEFINITION,
			    WORD: DEFINITION,
			    ...}

Updated 2.1
===========
- Added new words to the 'Space' category
- Reduced the score deducted from asking a hint from 1 point to 0.5 points
- Added flavor texts whenever a game ends