#! /usr/bin/env python3

import pdf_processor, texting
import time

pfdproc = pdf_processor.PdfProcessor()

while True:

    Questions = pfdproc.getQuestion()
    message = ''
    for Question in Questions:
        message =  message + Question
    print('The message char size: ' + str(len(message)) )
    
    if len(message) < 300:
        print('This will need to be fixed eventually.')
    elif len(message) <= 1600:
        message = message + 'Subject: ' + pfdproc.getSubject()
        print(texting.text_msg(message)) 
        time.sleep(900)
    else: 
        for Question in Questions:
            while len(message) < 1600:
                message =  message + Question
            
        message = message + 'Subject: ' + pfdproc.getSubject()
        print(texting.text_msg(message))
        time.sleep(900)

    
        
    




