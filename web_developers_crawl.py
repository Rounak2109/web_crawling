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
    position_1=1
    position_2=1
    position_3=1
    position_4=1
    position_5=1
    position_6=1
    position_7=1
    position_8=1
    position_9=1
    url_count=1
    #website=requests.get(page_url)
    #page=html.fromstring(website.content)
    #eview=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
    #urls=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')    
    #location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "provider-row", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
    #location2=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "provider-row", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
    for i in range(250):
        if i is 0:
            link= page_url
        else:
            link= page_url + '?page={}'.format(i)
        column=9
        worksheet.write(last,column,link)
        last+=1
        website=requests.get(link)
        page=html.fromstring(website.content)
        company_name=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "company-name", " " ))]//a/text()')
        review=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
        location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "location-city", " " ))]//span/text()')
        tagline=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tagline", " " ))]/text()')
        hourly_charge=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
        employees_count=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()')
        project_size=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        quote= page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "blockquote-in-module", " " ))]//p/text()')
        #company_links=page.xpath('/html/body/table/tbody/tr[409]/td[2]/span/a/text()')
        #href_link=page.xpath('//h3/a/text()')
        #urls=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        #urls=page.xpath('//*[contains(concat( " ", @class, " " ),concat(" ", "real-url"," "))]/text()')
        #urls=page.xpath('/a/span[@class= "Visit Website"]/@realurl')
        #urls=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sl-ext", " " ))]/text()')
        #urls=page.xpath('//*[text()="Visit Website"]')
        #urls=page.xpath('//a[@href="com"]/@realurl')
        urls=page.xpath('//li[@class = "website-link website-link-a"]/a/@href')
        #print(urls)
        list1=[]

        for items in urls:
            column=10
            worksheet.write(position_9,column,items)
            position_9+=1
            print("success_company_links %s" %position_9)

        for items in company_name:
            column=0
            #pass
            worksheet.write(rows,column,items)
            rows+=1
            print('success_company_name %s' %rows)
        
        for items in review:
            column=1
            worksheet.write(position_1,column,items)
            position_1+=1
            print('success_review %s' %position_1)
        
        s=0
        while(s < len(hourly_charge)):
            column=7
            print(hourly_charge[s].rstrip("\n\r"))
            worksheet.write(position_2,column,hourly_charge[s].rstrip("\n\r"))
            position_2+=1
            s+=1
            print("success_hourlycharge %s" %position_2)
        
        s=0
        position=1
        while(s < len(location)-1):
            column=2
            worksheet.write(position_3,column,location[s])
            worksheet.write(position_3,column+1,location[s+1])
            position_3+=1
            s+=2
            print('success_location %s' %position_3)
        
        s=0
        while(s < len(employees_count)):
            column=8
            worksheet.write(position_4,column,employees_count[s])
            position_4+=1
            s+=1
            print("success_employee_count %s" %position_4)

        s=0
        while(s < len(tagline)):
            column=4
            worksheet.write(position_5, column, tagline[s])
            position_5+=1
            s+=1
            print("success_tagline %s" %position_5)

        s=0
        while(s < len(project_size)):
            column=6
            worksheet.write(position_6, column, project_size[s].rstrip("\n\r"))
            position_6+=1
            s+=1
            print("success_projectsize %s" %position_6)

        s=0
        while(s < len(quote)):
            column=5
            worksheet.write(position_7, column, quote[s])
            position_7+=1
            s+=1
            print("success_quote %s" %position_7)

        print('completed page=%s' %i)

    workbook.close()
    
    return company_name


page_url= 'https://clutch.co/web-developers'
print(crawl(page_url))
