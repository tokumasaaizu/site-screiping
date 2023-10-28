# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime

def main():
    #try:
    #2次元配列の初期化
    contents_list = []

    info = 'マイナビ転職'
    target_url = 'https://tenshoku.mynavi.jp/list/i05260/f200/e01/ckw%E7%8B%AC%E7%AB%8B%E8%A1%8C%E6%94%BF%E6%B3%95%E4%BA%BA/?jobsearchType=4&searchType=8'
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, "html.parser")
    #1ページ内の URL、タイトル情報
    contents = soup.select('div.container__inner > div.cassetteRecruit')
    contents_count = len(contents)
    # class名は「.」で表現できる。
    site_title = soup.select('div.container__inner > div.cassetteRecruit > div > section > h3')
    site_employee = soup.select('div.container__inner > div.cassetteRecruit > div > section > p > span')
    site_url = soup.select('div.container__inner > div.cassetteRecruit > div > section > p > a')
    site_startday = soup.select('div.container__inner > div.cassetteRecruit > div.cassetteRecruit__content > div.cassetteRecruit__bottom > p.cassetteRecruit__updateDate > span')
    site_endday = soup.select('div.container__inner > div.cassetteRecruit > div.cassetteRecruit__content > div.cassetteRecruit__bottom > p.cassetteRecruit__endDate > span')
    for i in range(contents_count):
        title = site_title[i].contents[0]
        one_content_day = site_startday[i].contents[0]
        one_content_day = re.findall(r'\d+', one_content_day)
        start_day = one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2]
        end_day = site_endday[i].contents[0]
        date = datetime.strptime(end_day, '%Y/%m/%d')
        url = 'https://tenshoku.mynavi.jp/'+site_url[i].attrs['href']
        employee = site_employee[i].contents[0]
        if '独立行政法人' in title and '地方独立行政法人' not in title:
            contents_list.append([start_day,title,url,date,info,employee])

    info = 'マイナビ転職'
    target_url = 'https://tenshoku.mynavi.jp/list/e01+e02/ckw%E5%9B%BD%E7%AB%8B%E7%A0%94%E7%A9%B6%E9%96%8B%E7%99%BA%E6%B3%95%E4%BA%BA/?jobsearchType=14&searchType=18&refLoc=fnc_sra'
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, "html.parser")
    #1ページ内の URL、タイトル情報
    contents = soup.select('div.container__inner > div.cassetteRecruit')
    contents_count = len(contents)
    # class名は「.」で表現できる。
    #site_time = soup.select('div.list > a > article > div > div > div > span.post-date')
    #site_title = soup.select('div.list > a > article > div > h2')
    site_title = soup.select('div.container__inner > div.cassetteRecruit > div > section > h3')
    site_employee = soup.select('div.container__inner > div.cassetteRecruit > div > section > p > span')
    site_url = soup.select('div.container__inner > div.cassetteRecruit > div > section > p > a')
    site_startday = soup.select('div.container__inner > div.cassetteRecruit > div.cassetteRecruit__content > div.cassetteRecruit__bottom > p.cassetteRecruit__updateDate > span')
    site_endday = soup.select('div.container__inner > div.cassetteRecruit > div.cassetteRecruit__content > div.cassetteRecruit__bottom > p.cassetteRecruit__endDate > span')
    for i in range(contents_count):
        title = site_title[i].contents[0]
        one_content_day = site_startday[i].contents[0]
        one_content_day = re.findall(r'\d+', one_content_day)
        start_day = one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2]
        end_day = site_endday[i].contents[0]
        date = datetime.strptime(end_day, '%Y/%m/%d')
        url = 'https://tenshoku.mynavi.jp/'+site_url[i].attrs['href']
        employee = site_employee[i].contents[0]
        if '国立研究開発法人' in title:
            contents_list.append([start_day,title,url,date,info,employee])

    info = 'リクナビNEXT'
    count = 0
    target_url = 'https://next.rikunabi.com/kw%93%C6%97%A7%8Ds%90%AD%96%2540%90l/crn1.html?employ_frm_cd=01&searchdiv=1&l_abstruct_cond=0&keywordsearch=1&log_f=1'
    while True:
        res = requests.get(target_url)
        soup = BeautifulSoup(res.content, "html.parser")
        #1ページ内の URL、タイトル情報
        if count != 0:
            if count == 200:
                break
        contents = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > h2 > a')
        contents_employee = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > div > ul > li > span.rnn-label.rnn-label--small.rnn-label--steelBlue')
        #contents_employee = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > div > ul > li > span.rnn-label')
        contents_url = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > p')
        #contents = soup.select('body > div.rnn-SpWrapper.js-spWrapper > div:nth-child(12) > ul.rnn-group.rnn-group--xm.rnn-jobOfferList.js-floatSearchBox__limitTop.js-article > li:nth-child(1) > div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > h2 > a')
        contents_count = len(contents)
        for i in range(contents_count):
            url = contents[i].attrs['href']
            url = 'https://next.rikunabi.com'+url
            res2 = requests.get(url)
            soup2 = BeautifulSoup(res2.content, "html.parser")
            one_content = soup2.select('div.rn3-companyOfferHeadBottom > div > div.rn3-companyOfferHeader__bottom > div.rn3-companyOfferHeader__dateGroup > p')
            if len(one_content)== 0:
                start_day = '不明'
                end_day = '不明'
            else:
                one_content_day = one_content[0].contents[0]
                one_content_day = re.findall(r'\d+', one_content_day)
                start_day = one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2]
                end_day = one_content_day[3]+'/'+one_content_day[4]+'/'+one_content_day[5]
                date = datetime.strptime(end_day, '%Y/%m/%d')
            title = contents_url[i].contents[0]
            employee = contents_employee[i].contents[0]
            if '独立行政法人' in title and '地方独立行政法人' not in title:
                print(employee)
                contents_list.append([start_day,title,url,date,info,employee])
        count += 50
        target_url = 'https://next.rikunabi.com/kw%93%C6%97%A7%8Ds%90%AD%96%2540%90l/crn'+str(count+1)+'.html?employ_frm_cd=01&searchdiv=1&l_abstruct_cond=0&keywordsearch=1&log_f=1'

    info = 'リクナビNEXT'
    count = 0
    target_url = 'https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?keyword=%8D%91%97%A7%8C%A4%8B%86%8A%4A%94%AD%96%40%90%6C&employ_frm_cd=01&employ_frm_cd=03&curnum=1'
    while True:
        res = requests.get(target_url)
        soup = BeautifulSoup(res.content, "html.parser")
        #1ページ内の URL、タイトル情報
        if count != 0:
            if count == 50:
                break
        contents = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > h2 > a')
        contents_url = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > p')
        #contents_employee = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > div > ul > li > span.rnn-label.rnn-label--small.rnn-label--steelBlue')
        contents_employee = soup.select('div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > div > ul > li > span.rnn-label')
        result_employee = []
        for j in range(len(contents_employee)):
            if '契約社員' in contents_employee[j].contents[0]:
                result_employee.append(contents_employee[j].contents[0])
            if '正社員' in contents_employee[j].contents[0]:
                result_employee.append(contents_employee[j].contents[0])
        #contents = soup.select('body > div.rnn-SpWrapper.js-spWrapper > div:nth-child(12) > ul.rnn-group.rnn-group--xm.rnn-jobOfferList.js-floatSearchBox__limitTop.js-article > li:nth-child(1) > div.rnn-group.rnn-group--xxs.rnn-jobOfferList__item__company > h2 > a')
        contents_count = len(contents)
        contents_time = soup.select('div.rnn-jobOfferList__item__button > div > div > p > span')
        end_day = soup.select('ul.rnn-group.rnn-group--xm.rnn-jobOfferList.js-floatSearchBox__limitTop.js-article > li')
        for i in range(contents_count):
            url = contents[i].attrs['href']
            url = 'https://next.rikunabi.com'+url
            res2 = requests.get(url)
            soup2 = BeautifulSoup(res2.content, "html.parser")
            one_content = soup2.select('div.rn3-companyOfferHeadBottom > div > div.rn3-companyOfferHeader__bottom > div.rn3-companyOfferHeader__dateGroup > p')
            '''contents_employee = soup2.select('div.rn3-companyOfferHeader.rn3-stage > div > ul > li.rn3-tag.rn3-tag--employType')
            if 'https://next.rikunabi.com/rnc/docs/' in url:
                res3 = requests.get(url)
                soup3 = BeautifulSoup(res3.text, "html.parser")
                contents_employee = soup3.select('div.rnn-label--steelBlue')'''
            #employee = contents_employee[i].contents[0]
            #print(employee)
            #print(i)
            #if '契約社員' in employee:
                #employee = '契約社員'
            #if '正社員' in employee:
                #employee = '正社員'
            #print(employee)    
            if len(one_content)== 0:
                start_day = '不明'
                end_day = '不明'
            else:
                one_content_day = one_content[0].contents[0]
                one_content_day = re.findall(r'\d+', one_content_day)
                start_day = one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2]
                end_day = one_content_day[3]+'/'+one_content_day[4]+'/'+one_content_day[5]
                date = datetime.strptime(end_day, '%Y/%m/%d')
            title = contents_url[i].contents[0]
            if '国立研究開発法人' in title:
                print(result_employee[i])
                contents_list.append([start_day,title,url,date,info,result_employee[i]])
        count += 50
        target_url = 'https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?keyword=%8D%91%97%A7%8C%A4%8B%86%8A%4A%94%AD%96%40%90%6C&employ_frm_cd=01&employ_frm_cd=03&curnum='+str(count+1)
        
    info ='doda'
    target_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?k=%E7%8B%AC%E7%AB%8B%E8%A1%8C%E6%94%BF%E6%B3%95%E4%BA%BA&kwc=2&ind=22L%2C23L&ss=1&op=17&pic=1&ds=0&tp=1&bf=1&mpsc_sid=10&oldestDayWdtno=0&leftPanelType=1&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_showImageConditions_image'
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.select('div > div.upper.clrFix > h2 > a')
    contents_employee = soup.select('div > div.icons > ul > li.icoType')
    contents_title = soup.select('div > div.upper.clrFix > h2 > a > span.company.width688')
    for i in range(len(contents)):
        url = contents[i].attrs['href']
        res2 = requests.get(url)
        soup2 = BeautifulSoup(res2.content, "html.parser")
        one_content = soup2.select('h1')
        one_content_day = soup2.select('div.meta_head > div > p')[0].contents[0]
        one_content_day = re.findall(r'\d+', one_content_day)
        title = one_content[0].contents[0]
        end_day = one_content_day[3]+'/'+one_content_day[4]+'/'+one_content_day[5]
        date = datetime.strptime(end_day, '%Y/%m/%d')
        employee = contents_employee[i].contents[0]
        if '独立行政法人' in title and '地方独立行政法人' not in title:
            contents_list.append([one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2],title,url,date,info,employee])

    info ='doda'
    target_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?k=%E5%9B%BD%E7%AB%8B%E7%A0%94%E7%A9%B6%E9%96%8B%E7%99%BA%E6%B3%95%E4%BA%BA&kwc=2&ss=1&pic=1&ds=0&tp=1&bf=1&mpsc_sid=10&oldestDayWdtno=0&leftPanelType=1&usrclk_searchList=PC-logoutJobSearchList_searchConditionArea_searchButtonFloat-kwdInclude'
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.select('div > div.upper.clrFix > h2 > a')
    contents_employee = soup.select('div > div.icons > ul > li.icoType')
    contents_title = soup.select('div > div.upper.clrFix > h2 > a > span.company.width688')
    for i in range(len(contents)):
        url = contents[i].attrs['href']
        res2 = requests.get(url)
        soup2 = BeautifulSoup(res2.content, "html.parser")
        one_content = soup2.select('h1')
        one_content_day = soup2.select('div.meta_head > div > p')[0].contents[0]
        one_content_day = re.findall(r'\d+', one_content_day)
        title = one_content[0].contents[0]
        end_day = one_content_day[3]+'/'+one_content_day[4]+'/'+one_content_day[5]
        date = datetime.strptime(end_day, '%Y/%m/%d')
        employee = contents_employee[i].contents[0]
        if '国立研究開発法人' in title:
            contents_list.append([one_content_day[0][2:]+'/'+one_content_day[1]+'/'+one_content_day[2],title,url,date,info,employee])


    return contents_list

def CsvHeader(csv_file):
        with open(csv_file, 'w', encoding='utf-8',newline='') as f:
            header = '掲載日','法人名','URL','応募期限（掲載終了日）','情報元サイト', '雇用形態'
            writer = csv.writer(f)
            writer.writerow(header)

def OutputCsv(result_list, csv_file):
        #csv読み込み
        rows = []
        # サイズの大きいcsvファイルを読み込むために以下の記述が必要。
        csv.field_size_limit(1000000000)
        with open(csv_file, 'r', encoding='utf-8') as f_in:
            reader = csv.reader((line.replace('\0','') for line in f_in))
            for row in reader:
                rows.append(row)
        #ワークブック(csvファイル)への書き込み
        for i in range(len(result_list)):
            with open(csv_file, 'w', encoding='utf-8', newline="") as f:
                writer = csv.writer(f,lineterminator="\n")
                for data in rows:
                    writer.writerow(data) 
                writer.writerow([result_list[0],result_list[1],result_list[2],result_list[3],result_list[4],result_list[5]])

if __name__ == '__main__':
    csv_file = './output.csv'
    contents_list = main()
    for i in range(len(contents_list)):
        if contents_list[i][0] == '不明':
            most_early_day = '2050/01/01'
            contents_list[i][3] = datetime.strptime(most_early_day, '%Y/%m/%d')
    sorted_contents_list = sorted(contents_list, key=lambda s: s[3])
    #日付を「yyyy/mm/dd」から「yy/mm/dd」にする。また応募開始日が「不明」の場合は期限も「不明」とする。
    for i in range(len(sorted_contents_list)):
        if sorted_contents_list[i][0] == '不明':
            sorted_contents_list[i][3] = '不明'
        else:
            tstr = sorted_contents_list[i][3].strftime('%Y/%m/%d')
            separate_day = re.findall(r'\d+', tstr)
            sorted_contents_list[i][3] = separate_day[0][2:]+'/'+separate_day[1]+'/'+separate_day[2]
        # \r, \n 半角・全角スペースを削除
        data_ver2 = re.sub('\r','',sorted_contents_list[i][1])
        data_ver3 = re.sub('\n','',data_ver2)
        data_ver4 = re.sub('[  ]+',' ',data_ver3)
        sorted_contents_list[i][1] = data_ver4
    CsvHeader(csv_file)
    for i in range(len(sorted_contents_list)):
        OutputCsv(sorted_contents_list[i],csv_file)


