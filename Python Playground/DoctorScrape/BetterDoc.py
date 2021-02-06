#! /usr/bin/env python3

import SaDoctors
import re, bs4
import openpyxl

doctor = SaDoctors.ScrapeWeb()
Name_tag = 'h1'
Number_tag = 'a'
Speciality_tag = '.breadcrumb'
Number_re = re.compile(r'(\d+\s*)+')
Numbers_found = ''
Prac_details = []

email_list = open("DoctorsAPPPracttitioners.txt", "a")
wb = openpyxl.Workbook()
email_list.write('I hope this helps.\n\n')
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'Name'
sheet['B1'] = 'Number'
sheet['c1'] = 'Area + Speciality'



for k in range(1,69697,100):
    for i in range(k,k + 101):
        url = 'https://www.sadoctorsapp.co.za/Practitioner/' + str(i)
        Practition_page = doctor.getPage(url)
        doctor.setPageList(Practition_page, Name_tag)
        Name_List = doctor.getPageList()
        doctor.setPageList(Practition_page, Number_tag)
        Number_List = doctor.getPageList()
        doctor.setPageList(Practition_page, Speciality_tag)
        Speciality_List = doctor.getPageList()

        for j in Number_List:
            Numbers_ha = Number_re.search(str(j))
            if Numbers_ha != None:
                if len(Numbers_ha.group()) >= 10:
                    Numbers_found = Numbers_ha.group()
                    
        if Speciality_List != [] and Name_List != [] and Numbers_found != 0:
            Prac_details.append('Name: ' + Name_List[0].getText() + '\n' + 'Number: ' + Numbers_found + '\n' +
                            'Speciality: ' + Speciality_List[0].getText()[13:-1] + '\n')
            sheet['A'+ str(i+1)] = Name_List[0].getText()
            sheet['B'+ str(i+1)] = Numbers_found 
            sheet['C'+ str(i+1)] = Speciality_List[0].getText()[13:-1]

            print(Name_List[0].getText())
            print(Numbers_found)
            print(Speciality_List[0].getText()[13:-1])

    #for i in Prac_details:
        #print(i + '\n')
        #email_list.write(i + '\n')

    wb.save('SADoctersSpreadsheet.xlsx')

email_list.close()