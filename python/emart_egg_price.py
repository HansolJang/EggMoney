#-*- coding: utf-8 -*-
import urllib
from util.format_util import utils
from bs4 import BeautifulSoup
from config.db_config import db_conn
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

        sql = "INSERT INTO emart_egg_money (customer_price, date, product_title, product_thumb) VALUES (%s,now(),%s,%s)"
        params = utils.numberChange(customer_price.text), product_title.text, product_thumbnail.img.get('src').replace('//', '')
        cursors.execute(sql, (params))
        print(params)
        time.sleep(0.3)
        db_conn.commit()










