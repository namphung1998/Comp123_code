#  HW4 code file
## Nam Phung
## COMP123 - 03

import turtle
import random


# Question 1
#A - C - D

# Question 2
def sportsScore(dict, lst):
    """a function that calculates the score of a sport team"""
    score = 0
    for i in lst:
        score = score + dict[i]
    return score

# Question 3
def badWordFilter(str,lst):
    """a function that censors the bad words from a given sentence"""
    for word in lst:
        if word in str:
            str = str.replace(word, "<CENSORED>")
    return str

#print(badWordFilter('I have a cat and a dog', ['cat','dog']))






# Question 4

import string


def scrapeNames(text):
    """Takes in a string of text, and splits it into words.  It collect capitalized words in a dictionary
    that keeps track of how often the capitalized words occurred in the text."""
    nameDict = {} #wrong syntax for defining a dictionary
    words = clean(text.split()) #lacks () after split
    for word in words:
        firstLetter = word[0] #first letter's index should be 0 instead of 1
        if firstLetter.isupper():
            if word in nameDict:
                nameDict[word] = nameDict[word] + 1
            else:
                nameDict[word] = 1
    return nameDict

    
    
def clean(wordList):
    """Takes in a list of words, and cleans them up: it removes punctuation from the beginning or
    ending of each word, and builds a new list with the results."""
    cleanList = []
    for word in wordList:
        newWord = word.strip(string.punctuation)
        cleanList.append(newWord) #the function aims to returning the new list instead of the input list
    return cleanList #the function should return the value






