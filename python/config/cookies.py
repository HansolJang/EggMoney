import requests as rq
from config import url
import re



def cookie_parse(set_cookie):
    return re.sub('[^ ]+(?=,),', '', set_cookie).replace('  ', ' ')


def get_headers():
    custom_headers = {
        'Content-Type': 'text/html;charset=UTF-8',
        # 'User-Agent': 'Mozilla/5.0(compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Cookie': ''
    }
    res = rq.get(url['main'], headers=custom_headers)
    custom_headers['Cookie'] = cookie_parse(res.headers['Set-Cookie'])

    return custom_headers

if __name__ == '__main__':
    headers = get_headers()['Cookie']
