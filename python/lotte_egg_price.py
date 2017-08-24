#-*- coding: utf-8 -*-
import urllib
import re
from util.format_util import utils
from bs4 import BeautifulSoup
from config.db_config import db_conn
from config.config import lotte_url
import time
cursors = db_conn.cursor()

def lotte_scrapying():
    page = 0
    # while page <= 1:
    for url in lotte_url:
        source_code = urllib.urlopen(url)
        source = source_code.read()
        soup = BeautifulSoup(source, "lxml")
        container = soup.find('div', attrs={'class','wrap-tab-cont'})
        lis = container.find_all('article',attrs={'class','product-article'})[:12]
        # print product_title[0].text, customer_price[0].text
        # print product_thumbnail[0].img.get('src').replace('//','') # 썸네일 파싱
        egg_exclude_list = ['메추리알','구운','훈제']
        for item in lis:
            product_title = item.find('p', attrs={'class', 'prod-name'}) # 상품 이름
            customer_price = item.find('span', attrs={'class', 'num-n'}) # 상품 가격
            product_thumbnail = item.find('a', attrs={'class', 'thumb-link'}) # 상품 썸네일
            str_product_title = product_title.text.encode("UTF-8").strip()
            if egg_exclude_list[0] not in str_product_title and egg_exclude_list[1] not in str_product_title and \
                            egg_exclude_list[2] not in str_product_title:
                #egg_cnt = re.search('[0-9][0-9]', product_title.text)
                # 정규식이 10입 이상이면 되는데 한자리일때 오류 발생
                #one_egg_price = egg_cnt.group()

               # unit_price = int(utils.numberChange(customer_price.text)) / int(one_egg_price)
                select_sql = "SELECT count(*) from product where product_title=(%s)"
                cursors.execute(select_sql, str_product_title)
                print str_product_title
                row = cursors.fetchone()
                if row[0] == 0:
                    sql = "INSERT INTO product (sid, product_title, product_thumb, create_date) VALUES (3,%s,%s,now())"
                    params = str_product_title, product_thumbnail.img.get('src').replace('//', '')
                    cursors.execute(sql, (params))
                    print(params)
                    time.sleep(0.5)

                if row[0] == 1:
                    select_pid_sql = "SELECT pid from product where product_title=(%s)"
                    cursors.execute(select_pid_sql, str_product_title)
                    pid_row = cursors.fetchone()
                    print pid_row[0]

                    confirm_pid_sql = "SELECT count(*) from price where pid = (%s)"
                    cursors.execute(confirm_pid_sql, pid_row[0])
                    cnt_row = cursors.fetchone()
                    print cnt_row

                    if pid_row[0] > 0 and cnt_row[0] == 0:
                        price_sql = "INSERT INTO price (pid,customer_price,product_title, create_date) VALUES (%s,%s,%s,now())"
                        price_params = pid_row[0], utils.numberChange(customer_price.text), str_product_title
                        cursors.execute(price_sql, (price_params))
                        print price_params
                        time.sleep(3.0)
                db_conn.commit()
