#! /usr/bin/env python3

import bs4, requests, re
email_list = open("email_file.txt", "a")
email_list.write('I hope this helps. \n\n')
yello_reg = re.compile(r'.*@.*')

for i in range(150):
    web_url = "https://www.yellowpages.co.za/search?what=doctors&pg=" + str(i)
    yellow_pages = requests.get(web_url)
    yellow_pages.raise_for_status()
    yello_soup = bs4.BeautifulSoup(yellow_pages.text, "html.parser")
    yello_elems = yello_soup.select('span > .fullDetailId')


    for i in range(yello_elems.__len__()):
        email_yell = yello_reg.search(yello_elems[i].getText())
        if email_yell:
            email_list.write(email_yell.group() + '\n')
            print(email_yell.group())

email_list.close()