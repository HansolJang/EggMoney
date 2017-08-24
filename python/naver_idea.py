#-*- coding: utf-8 -*-
import urllib
import requests
import pymysql.cursors
from bs4 import BeautifulSoup

connection = pymysql.connect(host='127.0.0.1', user='root', password='zipdoc!@#', db='showdeco', charset='utf8')

def euc2utf(str):
    return unicode(str,'utf-8').encode('utf-8')

def spider(max_pages):
    page = 1
    while page <= max_pages:
       url = 'http://www.showdeco.co.kr/prg/inte/inte_real_order.asp?NPType=3&NowPage='+str(page)
       print(url)
       source_code = urllib.urlopen(url)
       soup = BeautifulSoup(source_code.read(),"lxml", from_encoding='euc-kr')
       table = soup.select('table > table:nth-child(2)')
       trs = table.tbody.find_all('tr')
       for tr in trs:
           tds = tr.find_all('td')
           create_date = tds[0].string
           estimate_name = tds[2].string
           customer_name = tds[3].string
           print(create_date, estimate_name, customer_name)
       page += 1


spider(1)