from lxml import html, etree
import requests
from io import StringIO, BytesIO
import os, xlsxwriter

def crawl(page_url):
    workbook= xlsxwriter.Workbook('companies_detail_it_services.xlsx')
    worksheet= workbook.add_worksheet()
    rows=1
    column=0
    position_1=1
    position_2=1
    position_3=1
    position_4=1
    position_5=1
    position_6=1
    position_7=1
    position_8=1
    position_9=1
    position_10=1
    for i in range(333):
        if i is 0:
            link= page_url
        else:
            link= page_url + '?page={}'.format(i)
        website=requests.get(link)
        page=html.fromstring(website.content)
        column=9
        worksheet.write(rows, column,link)
        rows+=1
        company_name=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "company-name", " " ))]//a/text()')
        reviews=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
        project_size=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        quote=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "blockquote-in-module", " " ))]//p/text()')
        location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "location-city", " " ))]//span/text()')
        hourly_charge=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
        tagline=page.xpath('//*[contains(concat( " ", @class, " "), concat( " ", "tagline", " "))]/text()')
        employee_count=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()')
        urls=page.xpath('//li[@class = "website-link website-link-a"]/a/@href')
        for items in company_name:
            column=0
            worksheet.write(position_1,column,items)
            position_1+=1
            print("success %s" %position_1)

        for items in reviews:
            column=1
            worksheet.write(position_2,column,items)
            position_2+=1
            print("success %s" %position_2)

        for items in tagline:
            column=2
            worksheet.write(position_3,column,items)
            position_3+=1
            print("success %s" %position_3)
        
        for items in quote:
            column=3
            worksheet.write(position_4,column,items)
            position_4+=1
            print("success %s" %position_4)
        
        s=0
        while(s < len(location)-1):
            column=4
            worksheet.write(position_5,column,location[s])
            worksheet.write(position_5,column+1,location[s+1])
            s+=2
            position_5+=1
            print("success %s" %position_5)

        s=0
        while(s < len(hourly_charge)):
            column=6
            print(hourly_charge[s].rstrip("\n\r"))
            worksheet.write(position_6,column,hourly_charge[s].rstrip("\n\r"))
            position_6+=1
            s+=1
            print("success_hourlycharge %s" %position_6)
        s=0
        while(s < len(project_size)):
            column=7
            print(project_size[s].rstrip("\n\r"))
            worksheet.write(position_7,column,project_size[s].rstrip("\n\r"))
            position_7+=1
            s+=1
            print("success_project_size %s" %position_7)

        for items in employee_count:
            column=8
            worksheet.write(position_8,column,items)
            position_8+=1
            print("success_employee_count %s" %position_8)

        for items in urls:
            column=10
            worksheet.write(position_9,column,items)
            position_9+=1
            print("success_urls %s" %position_9)
        
        print("completed page %s" %i)

    workbook.close()
    return urls
page_url='https://clutch.co/it-services'
print(crawl(page_url))