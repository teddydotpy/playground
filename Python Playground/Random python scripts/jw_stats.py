#! /usr/bin/env python3
import requests, bs4

Fact_val = []
main_url = 'https://www.jw.org/en/jehovahs-witnesses/worldwide/'
url_object = requests.get(main_url)
ofile = open('Statsjw.txt' , 'w')

soup = bs4.BeautifulSoup(url_object.text, features="html.parser")
countr_list = [a['href'] for a in soup.select('.aroundTheWorldCountriesList a')]

for i in countr_list:
    url = requests.get(i)
    soupy = bs4.BeautifulSoup(url.text, features="html.parser")
    print(str([j.getText() for j in soupy.select('.sidebarContentShaded h2')]) + str([i.getText() for i in soupy.select('.sidebarContentShaded li')]))
    ofile.write(str([j.getText() for j in soupy.select('.sidebarContentShaded h2')]) + str([i.getText() for i in soupy.select('.sidebarContentShaded li')]))
    Fact_val.append(soupy.select('.sidebarContentShaded'))

ofile.close()