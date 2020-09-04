from bs4 import BeautifulSoup
from lxml import html
import requests
import html2text
import scrapy
import pandas as pd
import csv
class HtmlPage:
    def __init__(self,pagelink):
        #print(pagelink)
        headers = {
        "Connection":"keep-alive",'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
        self.htmlpage = requests.get(str(pagelink),headers=headers)
      
        
        soup = BeautifulSoup(self.htmlpage.text,'lxml')
        body = soup.find('body')
        
        h = html2text.HTML2Text()
        h.ignore_links = True
        #print(body)
        self.pagetext = h.handle(body.text).encode('utf8')
        
    
    def getText(self):
        return self.pagetext
    def splitText(self):
        return self.pagetext.decode('utf8').split('.')

mypage = HtmlPage("https://www.insightcrime.org/news/analysis/criminal-governance-coronavirus-colombia/")

textlist = mypage.splitText()

import xlsxwriter
workbook = xlsxwriter.Workbook('article2.xlsx') 
worksheet = workbook.add_worksheet() 
i = 1
for item in textlist:
    worksheet.write('A'+str(i), item) 
    i +=1
workbook.close()
   