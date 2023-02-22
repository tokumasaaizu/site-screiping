# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from datetime import datetime
from datetime import date
import re
import time

def main():
    try:
        session = HTMLSession()
        #ページ数のカウント
        page_count = 0
        #2次元配列の初期化
        contents_list = []
        #無限ループ。日付が2022/12になったらストップ
        # #2023/1 ～2022/11まで取得したい場合は、下記の「if tdatetime.month == 12」の部分を「if tdatetime.month == 10」に変える
        while True:
            page_count += 1
            #URLからコンテンツ情報を取得
            target_url = 'http://brow2ing.com/'+'index-'+str(page_count)+'.html'
            res = session.get(target_url)
            site_url = res.html.find('.Entry__heading > .title > a')
            site_title = res.html.find('.title')
            site_comment = res.html.find('.Entry__meta > .Entry__comment > a')
            site_date = res.html.find('.Entry__date')
            contents_count = len(site_url)
            for i in range(contents_count):
                url = site_url[i].attrs['href']
                title = site_title[i].text
                comment = int(site_comment[i].text.replace('コメント',''))
                # もしコメントがない場合は、「0」と表記する
                if comment == '':
                    comment = 0
                #re.findall()はマッチするすべての部分を文字列のリストとして返す。
                time_list = re.findall(r'\d+', site_date[i].text)
                date_time = time_list[0]+'-'+time_list[1]+'-'+time_list[2]
                # str型から datetime型に変換
                tstr = date_time
                tdatetime = datetime.strptime(tstr, '%Y-%m-%d')
                # 「2022年の12月」になったら処理を終了
                if tdatetime.month == 12 and tdatetime.year == 2022:
                    break
                #タイトル、URL、日付(date, datetime)、コメント数の順にリストに挿入
                contents_list.append([title,url,tdatetime,comment])
                #time.sleep(1)
            else:
                continue
            break
    except Exception as e:
        print(e)
    finally:
        pass
    print(contents_list)

if __name__ == '__main__':
    main()

