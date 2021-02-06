#! /usr/bin/env python3

import SaDoctors
import re

doctor = SaDoctors.ScrapeWeb()
tag = 'h3'
Docter_tag = '.col-md-6'
Province_SA = ['eastern-cape', 'free-state', 'gauteng', 'kwaZulu-natal', 'limpopo', 'mpumalanga', 'north-west', 'northern-cape', 
                    'western-cape' ]
Spec_Province = Province_SA[2]
url = 'https://www.sadoctorsapp.co.za/doctors/' + Spec_Province
Province_Cities = []
Formatted_City = []
spec_docPAgeList = []
DocType_Len = 0

DocPage = doctor.getPage(url)
doctor.setPageList(DocPage, tag)
DocPageList = doctor.getPageList()

City_Name_re = re.compile(r'(\w*\s+)+')

for i in DocPageList:
    City_name = City_Name_re.search(str(i))
    if City_name.group() != ' ':
        Province_Cities.append(City_name.group().lower().strip())

for i in Province_Cities:
    Formatted_City.append(i.replace('\x20', '-'))

for i in range(len(Formatted_City)):
    DocType_url = 'https://www.sadoctorsapp.co.za/doctors/' + Spec_Province + '/' + Formatted_City[i]
    DocPage = doctor.getPage(DocType_url)
    doctor.setPageList(DocPage, tag)
    DocTypePAgeList = doctor.getPageList()
    DocType_Len = len(DocTypePAgeList)

for j in range(DocType_Len):
    DocPage_url = 'https://www.sadoctorsapp.co.za/Results?Category_ID=1&Speciality_ID=' + str(j) + '&Type=doctors&Province=' + Spec_Province + '&Location=' + Formatted_City[5]
    spec_Docpage = doctor.getPage(DocPage_url)
    doctor.setPageList(spec_Docpage, Docter_tag)
    spec_docPAgeList = doctor.getPageList()

print(spec_docPAgeList)