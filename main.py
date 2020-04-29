from words import wordlist
import random
import os
import sys

def getword():
  word = random.choice(wordlist)
  return word.upper()

def play(word):
  ui = "_"*len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  flag = len(word) + (len(word)/2)
  print("Let's guess the word!")
  print("It consist",len(word),"words")
  print(ui)
  print("\n")
  while not guessed and flag > 0:
    guess = input("Guess a word or letter: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guess the letter",guess)
      elif guess not in word:
        print(guess,"is not in the word.")
        guessed_letters.append(guess)
        flag-=1
      else:
        # os.system("clear")
        print("Good job",guess,"is in the word")
        guessed_letters.append(guess)
        wlist = list(ui)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          wlist[index] = guess
        ui = "".join(wlist)
        if "_" not in ui:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed the word",guess)
      elif guess!=word:
        print(guess,"is not the word")
        flag-=1
        guessed_words.append(guess)
      else:
        guessed = True
        ui = words
        print("Good job",guess,"is the word")
    else:
      print("Not a valid guess")
    print(ui)
    print("\n")
  if guessed:
    print("Congrats you guessed the word")


# def main():
word = getword()
play(word)
while input("Play again (Y/N) ?").upper() == "Y":
 word = getword()
 play(word)



