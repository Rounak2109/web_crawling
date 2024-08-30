import xlsxwriter
import requests
from lxml import html
import datetime


 
  
# # Start from the first cell. 
# # Rows and columns are zero indexed. 


def func(url):
    row = 1
    row1=1
    row2=1
    row3=1
    row4=1
    column = 0
    workbook=xlsxwriter.Workbook('python_org_jobs.xlsx')
    worksheet = workbook.add_worksheet()
    var=1
    while (var!=5):
        website=requests.get(url+'/jobs/?page='+str(var))
        data=html.fromstring(website.content)
        var+=1
        names=data.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "listing-company-name", " " ))]//a/text()')
        #company_name=data.xpath('//span[@class , "listing-company-name"]/text()')
        #company_name=data.xpath('//*[@id="content"]/div/section/div/ol/li[1]/h2/span[1]/text()')
        #company_name=data.xpath('//*[@id="content"]/div/section/div/ol/li[2]/h2/span[1]/text()')
        
        company_name=data.xpath('//*[@id="content"]/div/section/div/ol/li[position()<27]/h2/span[1]/text()')
        # print(company_name)
        # for company in company_name[2]:
        #     if re.split("\s",company):
        #        print (True)
        count=0
        for length in range(len(company_name)):
            #if length.split() !='':
            
            if len(company_name[length].split()) != 0:
                count+=1
                string1=''
                #print(company_name[length].split())
                for length2 in range(len(company_name[length].split())):
                    #list2.append(company_name[length].split()[length2])
                    string1+=company_name[length].split()[length2]
                    #print(company_name[length].split()[length2])
                worksheet.write(row3, column+1, string1)
                row3+=1
                #print(string1)
            

                #print(count)
        
        location=data.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "listing-location", " " ))]//a/text()')
        looking_for=data.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "listing-job-type", " " ))]/text()')
        referenced_links=data.xpath('//*[@id="content"]/div/section/div/ol/li[15]/h2/span[1]/a/text()')
        referenced_links=data.xpath('//h2/span/a/@href')
        website_link=data.xpath('/html/body/div/div[3]/div/section/article/div[1]/ul[3]/li[3]/a/@href')
        #print(website_link)
        #website2=data.xpath(url+referenced_links)
        for length in range(len(names)):
            
            worksheet.write(row, column, names[length])
            worksheet.write(row,column+4,location[length])
            
            
            #worksheet.write(row,column+2,looking_for[length])
            row+=1
            #print('success %d' %length)
        for i in range(len(referenced_links)):
            website2=requests.get(url+referenced_links[i])
            data2=html.fromstring(website2.content)
            if i%2==0:
                requirements=data2.xpath('//*[@id="content"]/div/section/article/div[1]/ul[3]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[2]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[5]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[7]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[4]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[6]/li[2]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[3]/li/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[5]/li/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[9]/li[2]/a/@href')
                restrictions=data2.xpath('//strong/text()')
                # company_website=data2.xpath('//li~//li+//li//*[contains(concat( " ", @class, " " ), concat( " ", "external", " " ))]/text()')
                #print(restrictions[2])
                #print(restrictions[3])
                company_website=data2.xpath('//*[@id="content"]/div/section/article/div[1]/ul[2]/li[3]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[5]/li[3]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[3]/li[3]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[4]/li[3]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[6]/li[3]/a/@href | //*[@id="content"]/div/section/article/div[1]/ul[7]/li[3]/a/@href')
                # company_website2=data2.xpath('//*[@id="content"]/div/section/article/div[1]/ul[5]/li[3]/a')
                worksheet.write(row1,column+3, url+referenced_links[i])
                worksheet.write(row1,column+6,requirements[0])
                worksheet.write(row1,column+7,restrictions[2])
                worksheet.write(row1,column+8,restrictions[3])
                if len(company_website) !=0:
                    worksheet.write(row1,column+2,company_website[0])
                else:
                    worksheet.write(row1,column+2,"Empty")
                print(company_website)
                row1+=1
            else:
                worksheet.write(row2,column+5,url+referenced_links[i])
                row2+=1
        for length in range(len(names)):
            now=datetime.datetime.now()
            worksheet.write(row4,column+9,now.strftime("%Y-%m-%d %H:%M"))
            row4+=1
        row4=1
        for length in range(len(names)):
            now=datetime.datetime.now()
            worksheet.write(row4,column+10,now.strftime("%Y-%m-%d %H:%M"))
            row4+=1
    workbook.close()
urls='https://www.python.org'
func(urls)
