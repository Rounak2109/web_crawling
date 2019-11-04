from lxml import html, etree
import requests
from io import StringIO, BytesIO
import os, xlsxwriter

def crawl(page_url):
    workbook= xlsxwriter.Workbook('companies_detail.xlsx')
    worksheet= workbook.add_worksheet()
    rows=1
    column=0
    last=1
    position=1
    url_count=1
    website=requests.get(page_url)
    page=html.fromstring(website.content)
    review=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
    urls=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')    
    #location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "provider-row", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
    #location2=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "provider-row", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
    
    for i in range(250):
        if i is 0:
            link= page_url
        else:
            link= page_url + '?page={}'.format(i)
        
        title=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "company-name", " " ))]//a/text()')
        review=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
        location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "location-city", " " ))]//span/text()')
        tagline=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tagline", " " ))]/text()')
        hourly_charge=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
        employees_count=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()')
        project_size=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        code= page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "blockquote-in-module", " " ))]//p/text()')
        href_link=page.xpath('//h3/a/text()')
        urls=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        website=requests.get(link)
        page=html.fromstring(website.content)
        
        for items in title:
            #pass
            worksheet.write(rows,column,items)
            rows+=1
            print('success %s' %rows)

        for items in review:
            column=1
            worksheet.write(last,column,items)
            last+=1
            print('success_review %s' %last)

        for items in urls:
            column=1
            worksheet.write(position,column,items)
            position+=1
            print('success_urls %s' %position)

        s=0
        while(s < len(hourly_charge)):
            column=5
            print(hourly_charge[s].rstrip("\n\r"))
            worksheet.write(position,column,hourly_charge[s].rstrip("\n\r"))
            position+=1
            s+=1
            print("success %s" %position)

        s=0
        while(s < len(location)):
            column=2
            worksheet.write(position,column,location[s])
            worksheet.write(position,column+1,location[s+1])
            position+=1
            s+=2
            print('success_tagline %s' %position)

        s=0
        while(s < len(employees_count)):
            column=2
            worksheet.write(position,column,employees_count[s])
            position+=1
            s+=1
            print("success %s" %position)
        print('completed page=%s' %i)
    s=0
    while(s < len(location)):
        column=2
        worksheet.write(position,column,location[s])
        worksheet.write(position,column+1,location[s+1])
        position+=1
        s+=2
        print('success_tagline %s' %position)    
    workbook.close()
    s=0
    while(s < len(employees_count)):
        column=2
        worksheet.write(position,column,employees_count[s])
        position+=1
        s+=1
        print("success %s" %position)
    s=0
    while(s < len(project_size)):
        column=3
        worksheet.write(position,column,project_size[s])
        position+=1
        s+=1
        print("success %s" %position)
    s=0
    while(s < len(code)):
        column=4
        worksheet.write(position,column,code[s])
        position+=1
        s+=1
        print("success %s" %position)
    
    workbook.close()
    return hourly_charge


page_url= 'https://clutch.co/web-developers'
print(crawl(page_url))
