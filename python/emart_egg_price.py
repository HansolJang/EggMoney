#-*- coding: utf-8 -*-
import urllib
from util.format_util import utils
from bs4 import BeautifulSoup
from config.db_config import db_conn
import re
cursors = db_conn.cursor()
import time

def emart_scrapying():
    page = 0
    # while page <= 1:
    url = 'http://emart.ssg.com/category/listCategoryItem.ssg?dispCtgId=0006110143'
    source_code = urllib.urlopen(url)
    source = source_code.read()
    soup = BeautifulSoup(source, "lxml")

    container = soup.find('table', attrs={'class','lst_item'})
    items = container.find_all('td', attrs={'class','item_emall'})[:16]
    for item in items:
        product_title = item.find('div', attrs={'class','title'})
        customer_price = item.find('div', attrs={'class','price'})
        product_thumbnail = item.find('div', attrs={'class','thm'})
        egg_exclude_list = ['메추리알', '구운', '훈제']
        egg_count_list =['6','10','12','15','18','24','30']
        str_product_title = product_title.text.encode("UTF-8").strip()
        if egg_exclude_list[0] not in str_product_title and egg_exclude_list[1] not in str_product_title and \
                        egg_exclude_list[2] not in str_product_title:
            str_product_title = product_title.get_text().encode("UTF-8").strip()
            index =0
            for mark in egg_count_list:
                index += 1
                if mark in str_product_title:
                    unit_price = int(utils.numberChange(customer_price.text)) / int(mark)
                    sql = "INSERT INTO emart_egg_money (customer_price, date, product_title, product_thumb, unit_price) VALUES (%s,now(),%s,%s,%s)"
                    params = utils.numberChange(customer_price.text), product_title.text, product_thumbnail.img.get(
                        'src').replace('//', ''), unit_price
                    cursors.execute(sql, (params))
                    print(params)
                    time.sleep(0.3)
                    db_conn.commit()











