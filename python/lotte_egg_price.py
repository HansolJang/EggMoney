#-*- coding: utf-8 -*-
import urllib
import re
from operator import eq
from util.format_util import utils
from bs4 import BeautifulSoup
from config.db_config import db_conn
import time
cursors = db_conn.cursor()

def lotte_scrapying():
    page = 0
    # while page <= 1:
    url = 'http://www.lottemart.com/category/categoryList.do?CategoryID=C00100140007'
    source_code = urllib.urlopen(url)
    source = source_code.read()
    soup = BeautifulSoup(source, "lxml")
    container = soup.find('div', attrs={'class','wrap-tab-cont'})
    lis = container.find_all('article',attrs={'class','product-article'})[:12]
    # print product_title[0].text, customer_price[0].text
    # print product_thumbnail[0].img.get('src').replace('//','') # 썸네일 파싱
    egg_exclude_list = ['메추리알','구운']
    for item in lis:
        product_title = item.find('p', attrs={'class', 'prod-name'})
        # str_product_title = product_title.text.encode("UTF-8").strip()
        customer_price = item.find('span', attrs={'class', 'num-n'})
        product_thumbnail = item.find('a', attrs={'class', 'thumb-link'})
        str_product_title = product_title.text.encode("UTF-8").strip()
        if '메추리' not in str_product_title:
            str_product_title = product_title.text.encode("UTF-8").strip()
            egg_cnt = re.search('[0-9][0-9]', product_title.text)
            one_egg_price = egg_cnt.group()
            print str_product_title
            unit_price = int(utils.numberChange(customer_price.text)) / int(one_egg_price)

            sql = "INSERT INTO lotte_egg_money (customer_price, date, product_title, product_thumb, unit_price) VALUES (%s,now(),%s,%s,%s)"
            params = utils.numberChange(customer_price.text), str_product_title, product_thumbnail.img.get(
                'src').replace('//', ''), unit_price
            cursors.execute(sql, (params))
            print(params)
            time.sleep(0.3)
            db_conn.commit()

