#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from config.db_config import db_conn
import re
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
    lis = container.find_all('li')[8:]
    # print product_title[0].text, customer_price[0].text
    # print product_thumbnail[0].img.get('src').replace('//','') # 썸네일 파싱
    for item in lis:
        egg_exclude_list = ['메추리','구운','훈제']
        product_title = item.find('a', attrs={'class', 'name'})
        customer_price = item.find('strong', attrs={'class', 'buy'})
        product_thumbnail = item.find('a', attrs={'class', 'thumb'})
        one_egg_price = item.find('span', attrs={'class','unit'})
        str_product_title = product_title.text.encode("UTF-8").strip()
        unit_price = utils.sub_str(one_egg_price.get_text().strip())
        if egg_exclude_list[0] not in str_product_title and egg_exclude_list[1] not in str_product_title and egg_exclude_list[2] not in str_product_title:
            sql = "INSERT INTO homeplus_egg_money (customer_price, date, product_title, product_thumb, unit_price) VALUES (%s,now(),%s,%s,%s)"
            params = utils.numberChange(customer_price.text), product_title.text, product_thumbnail.img.get(
                'src').replace('//', ''), unit_price
            cursors.execute(sql, (params))
            print(params)
            time.sleep(0.3)
            db_conn.commit()
        # print product_title.text
        # print customer_price.text
        # print product_thumbnail.img.get('src').replace('//','')
