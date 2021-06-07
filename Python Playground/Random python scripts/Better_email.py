#! /usr/bin/env python3

import bs4, requests, re

email_list = open("email_file.txt", "a")
email_list.write('I hope this helps.\n\n')

for i in range(100):
    web_url = "http://www.yellowpages.co.za/search?what=doctors&pg=" + str(i)
    yellow_pages = requests.get(web_url)
    yellow_pages.raise_for_status()
    yello_soup = bs4.BeautifulSoup(yellow_pages.text, "html.parser")
    yello_elems = yello_soup.select('span > .fullDetailId')
    whole_elem = yello_soup.select('.idBusinessCardType')
    name_elems = yello_soup.select('.nameOverflow')

    mail_reg = re.compile(r'.*@.*')
    number_reg = re.compile(r'tel')
    emails_ha = []
    Number_ha = []

    for i in range(len(whole_elem)):
        email_yell = mail_reg.search(yello_elems[i].getText())
        num_yell = number_reg.search(yello_elems[i].getText())
        Check_yell = mail_reg.search(whole_elem[i].getText())
        numCheck_yell =  number_reg.search(whole_elem[i].getText())
        if email_yell and Check_yell:
            emails_ha.append(email_yell.group())
        else:
            emails_ha.append('')

        if num_yell and Check_yell:
            Number_ha.append(num_yell.group())
        else:
            Number_ha.append('')

    # print(emails_ha)
    # print(Number_ha)

    for i in range(name_elems.__len__()):
        print(name_elems[i].getText())
        print('Email: ' + emails_ha[i])
        print('Number: ' + Number_ha[i])
        #email_list.write('Email: ' + email_yell.group() + '\n')''' 

email_list.close()