#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from config.db_config import db_conn
from util.format_util import utils
import time
cursors = db_conn.cursor()

def homeplus_scrapying():
    page = 0
    # while page <= 1:
    url = 'http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=40077'
    source_code = urllib.urlopen(url)
    source = source_code.read()
    soup = BeautifulSoup(source, "lxml")
    container = soup.find('div', attrs={'class','samll-exwrap'})
    lis = container.find_all('li')[4:]
    # print product_title[0].text, customer_price[0].text
    # print product_thumbnail[0].img.get('src').replace('//','') # 썸네일 파싱
    for item in lis:
        product_title = item.find('a', attrs={'class', 'name'})
        customer_price = item.find('strong', attrs={'class', 'buy'})
        product_thumbnail = item.find('a', attrs={'class', 'thumb'})
        # print product_title.text
        # print customer_price.text
        # print product_thumbnail.img.get('src').replace('//','')
        # sql = "INSERT INTO homeplus_egg_money (customer_price, date, product_title, product_thumb) VALUES (%s,now(),%s,%s)"
        # params = utils.numberChange(customer_price.text), product_title.text, product_thumbnail.img.get('src').replace('//', '')
        # cursors.execute(sql, (params))
        # print(params)
        # time.sleep(0.3)
        # db_conn.commit()
homeplus_scrapying()