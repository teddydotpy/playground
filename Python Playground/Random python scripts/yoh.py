#! /usr/bin/env python3
Test_Word = "You can have data without information, but you cannot have information without data."
LetterBuffer = list(Test_Word)
LetterFound = {}

while ' ' in LetterBuffer: LetterBuffer.remove(' ')
while '.' in LetterBuffer: LetterBuffer.remove('.')
while ',' in LetterBuffer: LetterBuffer.remove(',')

for i in LetterBuffer:
    if i != '0':
        LetterFound[str(i).lower()] = LetterFound.get(i.lower(), 0 ) + 1
    
for i, j in LetterFound.items():
    print(i + ' = ' + str(j))