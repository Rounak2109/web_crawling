from lxml import html, etree
import requests
from io import StringIO, BytesIO
import os, xlsxwriter,sys

def crawl():
    page_url="https://clutch.co/directory/mobile-application-developers"
    workbook= xlsxwriter.Workbook('companies_details_mobile_designers.xlsx')
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
    for i in range(250):
        if i is 0:
            link= page_url
        else:
            link = page_url + '?page={}'.format(i)
        column=9
        worksheet.write(rows,column,link)
        rows+=1
        website=requests.get(link)
        page=html.fromstring(website.content)
        company_name=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "company-name", " " ))]//a/text()')
        #company_name=page.xpath('//*[contains(concat(" ",@class, " "), concat( " " ,@company-name, " "))]//a/text()')
        review=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reviews-count", " " ))]//a/text()')
        #review=page.xpath('//*[contains(concat(" ",@class, " "),concat( " " ,"review-count", " "))]//a/text()')
        tagline=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tagline", " " ))]/text()')
        #tagline=page.xpath('//*[contains(concat(" ",@class, " "),concat( " ", "tagline", " "))]//a/text()')
        quote=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "blockquote-in-module", " " ))]//p/text()')
        employee_count=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()')
        project_size=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
        hourly_price=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
        location=page.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "location-city", " " ))]//span/text()')
        urls=page.xpath('//li[@class = "website-link website-link-a"]/a/@href')
        for items in company_name:
            column=0
            worksheet.write(position_1,column,items)
            position_1+=1
            print("success %s" %position_1)

        for items in review:
            column=1
            worksheet.write(position_2,column,items)
            position_2+=1
            print("success_review %s" %position_2)
        
        for items in tagline:
            column=2
            worksheet.write(position_3,column,items)
            position_3+=1
            print("success_tagline %s" %position_3)

        for items in quote:
            column=3
            worksheet.write(position_4,column,items)
            position_4+=1
            print("success_quote %s" %items)
        s=0
        while(s < len(location)-1):
            column=4
            worksheet.write(position_5,column,location[s])
            worksheet.write(position_5,column+1,location[s+1])
            position_5+=1
            s+=2
            print("success_location %s" %position_5)

        s=0
        while(s < len(project_size)):
            column=6
            worksheet.write(position_6,column,project_size[s].rstrip("\n\r"))
            position_6+=1
            s+=1
            print("success_project_size %s" %position_6)

        s=0
        while(s < len(hourly_price)):
            column=7
            worksheet.write(position_7,column,hourly_price[s].rstrip("\n\r"))
            position_7+=1
            s+=1
            print("success_hourly_size %s" %position_7)

        s=0
        while(s < len(employee_count)):
            column=8
            worksheet.write(position_8,column,employee_count[s])
            position_8+=1
            s+=1
            print("success_employee_count %s" %position_8)
        
        for items in urls:
            column=10
            worksheet.write(position_9,column,items)
            position_9+=1
            print("success_urls %s" %position_9)

        print("completed successfully %s" %i)
    workbook.close()
    return company_name

#page_url="https://clutch.co/directory/mobile-application-developers"
print(crawl())


# if __name__ == '__main__':
#     globals()[sys.argv[0]]()