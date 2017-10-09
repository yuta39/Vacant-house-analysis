import urllib.request
from bs4 import BeautifulSoup

base_url = 'http://www.fudousan.or.jp/system/'
top_url = 'http://www.fudousan.or.jp/system/?act=m&type=14'
base_price = 1000 #1000万円
f = open("./url.txt",'w')

#登録対象となるURLが入れられたリストを書き込む
#url_list:対象の物件のURL
#name:書き込むテキストの名前
def output_txt(name,url_list):
    pass

#対象のエレメントにまで狭めたところからURLを観ていく
#beautiful_object:狭めたエレメント
def jump_location_link(beautiful_object):
    location_url_list = [ base_url+link.get("href")[1:] for link in beautiful_object.findAll("a")]
    return location_url_list


def add_text_line(url):
    f.write(url+'\n')


#物件情報から値段を読み取り、指定の価格未満であればTrue
#そうでなければFalse
#target_price:物件の値段
#setting_price：見積もり値段　之よりも低くあって欲しい
#返り値はBoolean
def is_under_price(target_price,setting_price):
    target_price = target_price.split("億")
    if len(target_price)>1:
        return False
    target_price = target_price[0]
    target_price = target_price.split("万")[0]
    target_price = "".join(target_price.split(","))
    target_price = int(target_price)
    if target_price < setting_price:
        return True
    return False


#物件情報から値段を読み取り価格と詳細URLを取得する
#part:パースした一部
#返り値は値段とURL
def get_price_and_detail_url(part):
    target_price = part.findAll(class_="imp")[1].find("p").string
    target_detail_url = part.find(class_="text_midashi").find("a").get("href")
    target_detail_url = base_url + target_detail_url[1:]
    return target_price,target_detail_url

"""
urlパラメータ
n=100:100件まで表示
p=1:ページは１
"""
import chardet
#対象のURLを開いてHTMLを取得する
#url:ウェブサイトのURL
#返り値は対象のサイトのHTML
def get_html_data(url):
    try:
        data = urllib.request.urlopen(url).read()
        guess = chardet.detect(data)
        print(guess)
        unicode_data = data.decode(guess['encoding'])
        return unicode_data
    except UnicodeDecodeError:
        unicode_data = data.decode(guess['encoding'],'ignore')
        return unicode_data
    except TimeoutError:
        return get_html_data(url)

import sys
#各地区の物件詳細ページを読み込む
#url:地区のURL
#返り値：指定価格以下の物件の詳細URLのリスト
def read_page_of_used_houses(url,price):
    url = url + "&" + "n=100" + "&" + "p=1"
    try:
        html = get_html_data(url)
        soup = BeautifulSoup(str(html),"html5lib")
        parts = soup.findAll(class_="result_all_part")

        for part in parts:
            target_price,detail_url = get_price_and_detail_url(part)
            if is_under_price(target_price,price):
                print(target_price,detail_url)
                #$add_text_line(detail_url)
            else:
                break
    except UnicodeDecodeError:
        print(url,"[ERROR]")



#各都道府県のページを読み取り、地区のURLを獲得する
#url:県のURL
#返り値：この都道府県で物件が獲得できる地区のURLのリスト
def read_page_of_prefectures(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(str(html),"html5lib")
    area_text = soup.find(class_="area")
    return [ link for link in jump_location_link(area_text) ][:-1]

#全体のページを読み取り、各都道府県のURLを取得する
#返り値：全ての都道府県のURL
def read_page_of_top():
    html = urllib.request.urlopen(top_url).read()
    soup = BeautifulSoup(str(html),"html5lib")
    map_text = soup.find(class_='map-text')
    return [link for link in jump_location_link(map_text)]


if __name__ == "__main__":
    #read_page_of_top()
    #test_url = "http://www.fudousan.or.jp/system//?act=l&type=14&pref=05&stype=d&city[]=05212"
    #read_page_of_prefectures(test_url)
    #for l in read_page_of_top():
    #    for link in read_page_of_prefectures(l):
    #        read_page_of_used_houses(link,1000)
    #        print(link)
    #    print("-------------------")
    #f.close()
    test_url = 'http://www.fudousan.or.jp/system//?act=l&type=14&pref=01&stype=d&city[]=01109'
    read_page_of_used_houses(test_url,1000)
