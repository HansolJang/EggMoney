#-*- coding: utf-8 -*-
import urllib
import re
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
    egg_exclude_list = ['메추리알','구운','훈제']
    for item in lis:
        product_title = item.find('p', attrs={'class', 'prod-name'})
        # str_product_title = product_title.text.encode("UTF-8").strip()
        customer_price = item.find('span', attrs={'class', 'num-n'}) # 상품 가격
        product_thumbnail = item.find('a', attrs={'class', 'thumb-link'}) # 상품 썸네일
        str_product_title = product_title.text.encode("UTF-8").strip()
        if egg_exclude_list[0] not in str_product_title and egg_exclude_list[1] not in str_product_title and \
                        egg_exclude_list[2] not in str_product_title:
            # str_product_title = product_title.text.encode("UTF-8").strip() # 상품 제목
            egg_cnt = re.search('[0-9][0-9]', product_title.text)
            one_egg_price = egg_cnt.group()
            print str_product_title
            unit_price = int(utils.numberChange(customer_price.text)) / int(one_egg_price)
            select_sql = "SELECT count(*) from product where product_title=(%s)"
            cursors.execute(select_sql, str_product_title)
            row = cursors.fetchone()
            if row[0] == 1:
                select_pid_sql = "SELECT pid from product where product_title=(%s)"
                cursors.execute(select_pid_sql, str_product_title)
                pid_row = cursors.fetchone()
                print pid_row[0]
                if pid_row[0] > 0:
                    price_sql = "INSERT INTO price (pid,customer_price, unit_price, create_date) VALUES (%s,%s,%s,now())"
                    price_params = pid_row[0], utils.numberChange(customer_price.text), unit_price
                    cursors.execute(price_sql, (price_params))
                    print price_params
                    time.sleep(0.5)
            # sql = "INSERT INTO product (sid, product_title, product_thumb, create_date) VALUES (3,%s,%s,now())"
            # params = str_product_title, product_thumbnail.img.get('src').replace('//', '')
            # cursors.execute(sql, (params))
            # print(params)
            # time.sleep(0.3)
            db_conn.commit()
