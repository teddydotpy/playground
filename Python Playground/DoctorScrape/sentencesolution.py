#! /usr/bin/env python3

def mostWordsEndWith(sentence):
    
    sentence.replace('.', '')
    print(sentence)
    maxWord = 0
    wordPos = 0
    wordList = sentence.split(" ")

    for i in range(len(wordList)):
        wordFind = 0
        for j in range(len(wordList)):
            if wordList[i] == wordList[j]:
                wordFind += 1

        if maxWord < wordFind:
            wordPos = i
            maxWord = wordFind
    

    maxWordLetter = wordList[wordPos]
    wordLetterEnd = []

    for i in wordList:
        if i[-1] == maxWordLetter[-1]:
            wordLetterEnd.append(i)

    returnDictionary = {'letters':maxWordLetter[-1], 'words':wordLetterEnd}

    return returnDictionary


print(mostWordsEndWith('I am very stupid.')) 

    
