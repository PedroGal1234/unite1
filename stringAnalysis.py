#Pedro Gallino
#9/1/17
#stringAnalysis.py - discirbes a sentece

sentence = input('Enter a Sentence: ')
sentence = sentence.lower()

spaces = sentence.count(" ")
characters = len(sentence)
print('Your Sentence has',spaces+1,'words and',characters,'characters and',characters-(spaces),'letters.')

sentence.lower()
letter = input('Enter a Character to search for: ')
print('Your sentence has', sentence.count(letter),'of the character: ',letter)
word = input