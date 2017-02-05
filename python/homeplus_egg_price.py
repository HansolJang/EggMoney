#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from config.db_config import db_conn
import re
from util.format_util import utils
import time
cursors = db_conn.cursor()

#Todo - html 구조상 list[0] 다음에 list[4]으로 되어있어서 예외처리 추가해야함

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
        egg_exclude_list = ['메추리','구운','훈제']
        product_title = item.find('a', attrs={'class', 'name'})
        customer_price = item.find('strong', attrs={'class', 'buy'})
        product_thumbnail = item.find('a', attrs={'class', 'thumb'})
        one_egg_price = item.find('span', attrs={'class','unit'})
        str_product_title = product_title.text.encode("UTF-8").strip()
        unit_price = utils.sub_str(one_egg_price.get_text().strip())
        if egg_exclude_list[0] not in str_product_title and egg_exclude_list[1] not in str_product_title and egg_exclude_list[2] not in str_product_title:
            # sql = "INSERT INTO homeplus_egg_money (customer_price, date, product_title, product_thumb, unit_price) VALUES (%s,now(),%s,%s,%s)"
            # params = utils.numberChange(customer_price.text), product_title.text, product_thumbnail.img.get(
            #     'src').replace('//', ''), unit_price
            # cursors.execute(sql, (params))
            # print(params)
            # time.sleep(0.3)
            # db_conn.commit()
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
                    price_params =  pid_row[0],utils.numberChange(customer_price.text), unit_price
                    cursors.execute(price_sql,(price_params))
                    print price_params
                    time.sleep(0.5)
            # sql = "INSERT INTO product (sid, product_title, product_thumb, create_date) VALUES (1,%s,%s,now())"
            # params = str_product_title, product_thumbnail.img.get('src').replace('//', '')
            # cursors.execute(sql, (params))
            # print(params)
            # db_conn.insert_id()
            # pid = cursors.lastrowid
            # price_sql = "INSERT INTO price (pid,customer_price, unit_price, create_date) VALUES (%s,%s,%s,now())"
            # price_params =  pid,utils.numberChange(customer_price.text), unit_price
            # cursors.execute(price_sql,(price_params))
            # print price_params
            # time.sleep(0.5)
            db_conn.commit()

