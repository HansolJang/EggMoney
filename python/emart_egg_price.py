#-*- coding: utf-8 -*-
import urllib
from util.format_util import utils
from bs4 import BeautifulSoup
from config.db_config import db_conn
from config.config import emart_url
from requests.auth import HTTPBasicAuth
import requests
from requests_ntlm import HttpNtlmAuth
import re
import base64
import sys
cursors = db_conn.cursor()
import time


def emart_scrapying():
    page = 0
    # while page <= 1:
    for url_list in emart_url:
        url = url_list
        print url
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
                if mark in str_product_title:
                    unit_price = int(utils.numberChange(customer_price.text)) / int(mark)
                    select_sql = "SELECT count(*) from product where product_title=(%s)"
                    cursors.execute(select_sql, str_product_title)
                    row = cursors.fetchone()
                    if row[0] == 1:
                        select_pid_sql = "SELECT pid from product where product_title=(%s)"
                        cursors.execute(select_pid_sql, str_product_title)
                        pid_row = cursors.fetchone()
                        print pid_row[0]
                        if pid_row[0] > 0:
                            # price_sql = "INSERT INTO price (pid,customer_price, unit_price, create_date) VALUES (%s,%s,%s,now())"
                            # price_params = pid_row[0], utils.numberChange(customer_price.text), unit_price
                            # cursors.execute(price_sql, (price_params))
                            # print price_params
                            time.sleep(1.5)
                    # sql = "INSERT INTO product (sid, product_title, product_thumb, create_date) VALUES (2,%s,%s,now())"
                    # params = str_product_title, product_thumbnail.img.get('src').replace('//', '')
                    # cursors.execute(sql, (params))
                    # print(params)
                    # time.sleep(0.3)
                    # db_conn.commit()











