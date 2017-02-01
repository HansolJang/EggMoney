#-*- coding: utf-8 -*-
import urllib
import requests
import re
import pymysql.cursors
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from datetime import datetime
from config.db_config import db_conn
import time

def numberChange(str):
    return re.sub('[^0-9]','',str)

def euc2utf(str):
    return unicode(str,'utf-8').encode('utf-8')

def scrapying():
    page = 0
    # while page <= 1:
    url = 'http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=40077'
    source_code = urllib.urlopen(url)
    source = source_code.read()
    soup = BeautifulSoup(source, "lxml")
    container = soup.find('div', attrs={'class','samll-exwrap'})
    lis = container.find_all('li')
    # print product_title[0].text, customer_price[0].text
    # print product_thumbnail[0].img.get('src').replace('//','') # 썸네일 파싱
    for item in lis:
        product_title = item.find('a', attrs={'class', 'name'})
        customer_price = item.find('strong', attrs={'class', 'buy'})
        product_thumbnail = item.find('a', attrs={'class', 'thumb'})
        # print product_title.text
        # print customer_price.text
        # print product_thumbnail.img.get('src').replace('//','')
        with db_conn.cursor() as cursor:
            sql = "INSERT INTO homeplus_egg_money (customer_price, date, product_title, product_thumb) VALUES (%s,now(),%s,%s)"
            params = customer_price.text, product_title.text, product_thumbnail.img.get('src').replace('//', '')
            cursor.execute(sql, (params))
            print(params)
            time.sleep(0.3)
            db_conn.commit()


scrapying()