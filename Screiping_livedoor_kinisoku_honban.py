# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import re
import time

def main():
    try:
        #ページ数のカウント
        page_count = 0
        #2次元配列の初期化
        contents_list = []
        #無限ループ。日付が2022/12になったらストップ
        # #2023/1 ～2022/11まで取得したい場合は、下記の「if tdatetime.month == 12」の部分を「if tdatetime.month == 10」に変える
        while True:
            page_count += 1
            #URLからコンテンツ情報を取得
            target_url = 'http://blog.livedoor.jp/kinisoku/'+'?p='+str(page_count)
            res = requests.get(target_url)
            soup = BeautifulSoup(res.text, "html.parser")
            #1ページ内の URL、タイトル情報
            contents = soup.select('div.clearfix > div > div > h1 > a')
            contents_count = len(contents)
            site_comment = soup.select('div.clearfix > div > div > p.section_comment > a')
            site_time = soup.select('div.clearfix > div > div > ul > li.info_time')
            # 1ページ内にある新着記事の数分(6個)処理をする。処理が終わったら次ページへ。
            for i in range(contents_count):
                url = contents[i].attrs['href']
                title = contents[i].contents[0]
                comment = int(site_comment[i].contents[0])
                # もしコメントがない場合は、「0」と表記する
                if comment == '':
                    comment = 0
                #re.findall()はマッチするすべての部分を文字列のリストとして返す。
                time = site_time[0].contents[0]
                time_list = re.findall(r'\d+', time)
                date_time = time_list[0]+'-'+time_list[1]+'-'+time_list[2]+'-'+time_list[3]+'-'+time_list[4]
                # str型から datetime型に変換
                tstr = date_time
                tdatetime = datetime.strptime(tstr, '%Y-%m-%d-%H-%M')
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

