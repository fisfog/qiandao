# coding: utf-8

import requests
import re
import os

# if you don't have a config.py
# You can set xiami_username, xiami_password yourself

#xiami_username = os.getenv('xiami_username')
#xiami_password = os.getenv('xiami_password')
xiami_username = '243826245@qq.com'
xiami_password = 'myl09040416'


def qiandao_xiami():
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.57 Safari/537.36 OPR/40.0.2308.15 (Edition beta)',
                'Referer': 'http://www.xiami.com/web/login',
                'Origin': 'http://www.xiami.com/web'
              }
    session = requests.Session()
    session.headers.update(headers)

    resp = session.get('http://www.xiami.com/web/login')
    print(resp.text)
    
    u = re.findall(r'class="name"', resp.text)
    p = re.findall(r'class="password"', resp.text)

if __name__ == '__main__':
    qiandao_xiami()
