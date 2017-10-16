###################################################
#空き家バンクのページから掲載されている物件の情報を取得する
##################################################


from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import chardet
import time
import csv

base_url = "http://www.fudousan.or.jp/system/"
buy_url = "http://www.fudousan.or.jp/system/?act=ak&type=s1"
rent_url = "http://www.fudousan.or.jp/system/?act=ak&type=s3"
item_class_name = "uk-width-medium-1-3 itemBox" #トップページの空き家のclass名
detail_url_class_name = "uk-panel uk-panel-hover cnt-detail" #詳細ページが書かれているタグのクラス

#出力するCSVのカラム
csv_colums = ["物件番号","価格","所在地","交通","土地面積","建物面積",
                "間取り","間取り詳細","築年月","物件種目","敷地面積の権利形態",
                "借地料及び借地期間","権利金","その他の費用","地目","地勢","接道",
                "法令上の制限","国土法届出","都市計画","用途地域","建ぺい率",
                "容積率","私道面積","セットバック","構造","階数","駐車場",
                "現況","引渡し時期","線区画数","販売戸数","備考1","備考2","設備",
                "特記","取引対応","情報登録日"]

#対象のURLを開いてHTMLを取得する
#url:ウェブサイトのURL
#返り値は対象のサイトのHTML
def get_html_data(url):
    if url is not None:
        browser = webdriver.Chrome(driver_path) #Chromeブラウザを指定
        browser.implicitly_wait(10)
        browser.get(url) # URLへアクセス
        time.sleep(3) #読み込まれるまで待機
        return browser.page_source # アクセスしたサイトのページソースを返す


#ページのHTMLから現在取得可能な全ての物件を抽出する
def get_akiya_item(html):
    soup = BeautifulSoup(str(html),"html5lib")
    item_list = soup.findAll(class_=item_class_name)
    return item_list

#対象の空き家の詳細URLを取得する
def get_akiya_detail_page_url(item):
    #print(type(item))
    detail_item = item.find(class_=detail_url_class_name)
    return base_url + detail_item.get("href")

#価格の取得
def get_price(bs_obuject):
    return bs_obuject.find(id="d048").string

#物件番号
def get_object_number(bs_obuject):
    return bs_obuject.find(id="d003").string

#所在地
def get_object_location(bs_obuject):
    return bs_obuject.find(id="address").string

#交通
def get_route(bs_obuject):
    return bs_obuject.find(id="traffic").string

#土地面積
def get_land_space(bs_obuject):
    return bs_obuject.find(id="d127").string

#建物面積
def get_build_space(bs_obuject):
    return bs_obuject.find(id="d139").string

#間取り
def get_floor_plan(bs_obuject):
    return bs_obuject.find(id="madori").string

#間取り詳細
def get_floor_plan_detail(bs_obuject):
    return bs_obuject.find(id="madoriuchiwake").string

#築年月
def get_build_year(bs_obuject):
    return bs_obuject.find(id="d159").string

#物件種目
def get_object_space(bs_obuject):
    return bs_obuject.find(id="d635").string

#敷地面積の権利形態
def get_land_right_type(bs_obuject):
    return bs_obuject.find(id="d145").string

#借地料及び借地期間
def get_land_rent_and_perio(bs_obuject):
    return bs_obuject.find(id="d058").string

#権利金
def get_right_rate(bs_obuject):
    return bs_obuject.find(id="d078").string

#その他の費用
def get_other_price(bs_obuject):
    return bs_obuject.find(id="sonota").string

#地目
def get_classification_of_land(bs_obuject):
    return bs_obuject.find(id="d206").string

#地勢
def get_geographical_features(bs_obuject):
    return bs_obuject.find(id="d212").string

#接道
def get_adjacent_road(bs_obuject):
    return bs_obuject.find(id="d380").string

#法令上の制限
def get_laws_limitation(bs_obuject):
    return bs_obuject.find(id="d224").string

#国土法届け出
def get_countory_lows_submit(bs_obuject):
    return bs_obuject.find(id="d225").string

#都市計画
def get_city_planning(bs_obuject):
    return bs_obuject.find(id="d208").string

#用途地域
def get_used_land_type(bs_obuject):
    return bs_obuject.find(id="d210").string

#建ぺい率
def get_building_coverage(bs_obuject):
    return bs_obuject.find(id="d149").string

#容積率
def get_floor_area_ratio(bs_obuject):
    return bs_obuject.find(id="d150").string

#私道面積
def get_driveway_area(bs_obuject):
    return bs_obuject.find(id="d135").string

#セットバック
def get_set_back(bs_obuject):
    return bs_obuject.find(id="d339").string

#構造
def get_build_structure(bs_obuject):
    return bs_obuject.find(id="d151").string


#階数
def get_rank(bs_obuject):
    return bs_obuject.find(id="d154").string

#駐車場
def get_parking_area(bs_obuject):
    return bs_obuject.find(id="d386").string

#現況
def get_now_status(bs_obuject):
    return bs_obuject.find(id="d214").string

#引渡し時期
def get_move_timing(bs_obuject):
    return bs_obuject.find(id="d218").string

#線区画数
def get_total_number_of_compartments(bs_obuject):
    return bs_obuject.find(id="d157").string

#販売戸数
def get_unit_sold(bs_obuject):
    return bs_obuject.find(id="d158").string

#備考１
def get_remarks_1(bs_obuject):
    return bs_obuject.find(id="d415").string

#備考２
def get_remarks_2(bs_obuject):
    return bs_obuject.find(id="bikou2").string

#設備
def get_facility(bs_obuject):
    return bs_obuject.find(id="setsubi").string

#特記
def get_spetial_mention(bs_obuject):
    return bs_obuject.find(id="tokki").string

#取引対応
def get_object_space(bs_obuject):
    return bs_obuject.find(id="d114").string

#情報登録日
def get_add_page(bs_obuject):
    return bs_obuject.find(id="d419").string

def get_detail_date_tag(html):
    soup = BeautifulSoup(str(html),"html5lib")
    return soup.find(class_="uk-panel detailLists")

if __name__ == "__main__":
    #html = get_html_data(buy_url)
    #print(html)
    html = open("./sample.html").read()
    write_fp=csv.writer(open("./output_akiya.csv", "w"))
    write_fp.writerow(csv_colums)

    #空き家バンクのデータを書き込み
    for item in get_akiya_item(html):
        url = get_akiya_detail_page_url(item)
        html = get_html_data(url)
        soup_object = get_detail_date_tag(html)
        csv_output_row = [
        get_object_number(soup_object),get_price(soup_object),
        get_object_location(soup_object),get_route(soup_object),
        get_land_space(soup_object),get_build_space(soup_object),
        get_floor_plan(soup_object),get_floor_plan_detail(soup_object),
        get_build_year(soup_object),get_object_space(soup_object),
        get_land_right_type(soup_object),get_land_rent_and_perio(soup_object),
        get_right_rate(soup_object),get_other_price(soup_object),
        get_classification_of_land(soup_object),get_geographical_features(soup_object),
        get_adjacent_road(soup_object),get_laws_limitation(soup_object),
        get_countory_lows_submit(soup_object),get_city_planning(soup_object),
        get_used_land_type(soup_object),get_building_coverage(soup_object),
        get_floor_area_ratio(soup_object),get_driveway_area(soup_object),
        get_set_back(soup_object),
        get_build_structure(soup_object),get_rank(soup_object),
        get_parking_area(soup_object),get_now_status(soup_object),
        get_move_timing(soup_object),get_total_number_of_compartments(soup_object),
        get_unit_sold(soup_object),get_remarks_1(soup_object),
        get_remarks_2(soup_object),get_facility(soup_object),
        get_spetial_mention(soup_object),get_object_space(soup_object),
        get_add_page(soup_object)
        ]
        print(csv_output_row)
        write_fp.writerow(csv_output_row)
