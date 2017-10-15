
import urllib.request
import chardet
from bs4 import BeautifulSoup
import csv



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

def search_word(html,word):
    index = html.find(word) - 15
    html_part = html[index:index+100]
    soup = BeautifulSoup(str(html_part),"html5lib")
    print(soup)
    return soup.findAll("p")[1].string

#物件番号の取得
def get_object_number(html):
    index = html.find("物件番号") - 27
    html_part = html[index:index+100]
    soup = BeautifulSoup(str(html_part),"html5lib")
    return soup.findAll("p")[0].string.split("／")[0].split(":")[1]

#総合サイトの物件番号を取得
def get_all_site_object_number(html):
    index = html.find("物件番号") - 27
    html_part = html[index:index+100]
    soup = BeautifulSoup(str(html_part),"html5lib")
    return soup.findAll("p")[0].string.split("／")[1].split(":")[1]

#物件種目を取得
def get_build_type(html):
    result = search_word(html,"<p>物件種目</p>")
    print(result)
    return result


#敷地の権利種目を取得
def get_land_right_type(html):
    result = search_word(html,"<p>敷地の権利形態</p>")
    print(result)
    return result


#借地料と借地期間を取得
def get_land_rent_and_period(html):
    result = search_word(html,"<p>借地料および借地期間</p>")
    print(result)
    return result

#権利料を取得
def get_right_rate(html):
    result = search_word(html,"<p>権利金</p>")
    print(result)
    return result

#地目を取得
def get_classification_of_land(html):
    result = search_word(html,"<p>地目</p>")
    print(result)
    return result

#地勢を取得
def get_geographical_features(html):
    result = search_word(html,"<p>地勢</p>")
    print(result)
    return result

#接道を取得
def get_adjacent_road(html):
    result = search_word(html,"<p>接道</p>")
    print(result)
    return result

#法令上の制限を取得
def get_laws_limitation(html):
    result = search_word(html,"<p>法令上の制限</p>")
    print(result)
    return result

#国土法届出について取得
def get_countory_lows_submit(html):
    result = search_word(html,"<p>国土法届出</p>")
    print(result)
    return result

#都市計画について首都高
def get_city_planning(html):
    result = search_word(html,"<p>都市計画</p>")
    print(result)
    return result

#用途地域の取得
def get_used_land_type(html):
    result = search_word(html,"<p>用途地域</p>")
    print(result)
    return result


#建ぺい率の取得
def get_building_coverage(html):
    result = search_word(html,"<p>建ぺい率</p>")
    print(result)
    return result

#容積率の取得
def get_floor_area_ratio(html):
    result = search_word(html,"<p>容積率</p>")
    print(result)
    return result

#私道面積の取得
def get_driveway_area(html):
    result = search_word(html,"<p>私道面積</p>")
    print(result)
    return result

#セットバックの取得
def get_set_back(html):
    result = search_word(html,"<p>セットバック</p>")
    print(result)
    return result


#建物の構造種類を取得（木造かコンクリートかなど）
def get_build_structure(html):
    result = search_word(html,"<p>構造</p>")
    print(result)
    return result

#階数を取得する
def get_rank(html):
    result = search_word(html,"<p>階数</p>")
    print(result)
    return result

#駐車場の有無
def get_parking_area(html):
    result = search_word(html,"<p>駐車場</p>")
    print(result)
    return result

#総区画数の取得
def get_total_number_of_compartments(html):
    result = search_word(html,"<p>総区画数</p>")
    print(result)
    return result

#設備について取得
def get_facility(html):
    result = search_word(html,"<p>設備</p>")
    print(result)
    return result

#特記について取得
def get_spetial_mention(html):
    result = search_word(html,"<p>特記</p>")
    print(result)
    return result

#備考１を取得
def get_remarks_1(html):
    result = search_word(html,"<p>備考1</p>")
    print(result)
    return result

#備考２を取得
def get_remarks_2(html):
    result = search_word(html,"<p>備考2</p>")
    print(result)
    return result


#物件の価格を取得
def get_price(html):
    soup = BeautifulSoup(str(html),"html5lib")
    result = soup.find(class_="syousai_price").string[4:]
    print(result)
    return result

#所在地の取得
def get_path(html):
    soup = BeautifulSoup(str(html),"html5lib")
    result = soup.find(class_="address-cell").find("span").string
    print(result)
    return result

#交通に関しての情報を取得
def get_route(html):
    result = search_word(html,"<p>交通</p>")
    print(result)
    return result

#土地面積を取得
def get_land_space(html):
    result = search_word(html,"<p>土地面積</p>")
    print(result)
    return result

#建物面積を取得
def get_build_space(html):
    result = search_word(html,"<p>建物面積</p>")
    print(result)
    return result

#間取り情報を取得
def get_floor_plan(html):
    result = search_word(html,"<p>間取り</p>")
    print(result)
    return result

#間取りの詳細情報を取得
def get_floor_plan_detail(html):
    result = search_word(html,"<p>間取り内訳</p>")
    print(result)
    return result

#築年数を取得
def get_build_year(html):
    result = search_word(html,"<p>築年月</p>")
    print(result)
    return result

if __name__ == "__main__":
    #test_url = 'http://www.fudousan.or.jp/system//?act=d&type=14&pref=23&stype=d&city[]=23112&n=20&p=1&v=on&s=&bid=02927063&org=ZN'
    #print(get_html_data(test_url))
    f = open("./url.txt").readlines()
    write_fp=csv.writer(open("output.csv", "w"))
    csv_colums = [
        '物件番号','総合物件番号','物件種目','権利種目','権利金',
        '地目','地勢','接道','制限','国土法届出','都市計画','用途地域',
        '建ぺい率','容積率','私道面積','セットバック','構造種類','階数',
        '駐車場','総区画数','設備','特記','備考１','備考２','物件価格',
        '所在地','交通','土地面積','建物面積','間取り','間取りの内訳',
        '築年数'
    ]
    write_fp.writerow(csv_colums)

    for url in f:
        url = url[:-1]
        print(url)
        try:
            html = get_html_data(url)
            #各種データの取得
            csv_output_row = [
                get_object_number(html),get_all_site_object_number(html),get_build_type(html),
                get_land_right_type(html),get_right_rate(html),get_classification_of_land(html),
                get_geographical_features(html),get_adjacent_road(html),get_laws_limitation(html),
                get_countory_lows_submit(html),get_city_planning(html),get_used_land_type(html),
                get_building_coverage(html),get_floor_area_ratio(html),get_driveway_area(html),
                get_set_back(html),get_build_structure(html),get_rank(html),
                get_parking_area(html),get_total_number_of_compartments(html),get_facility(html),
                get_spetial_mention(html),get_remarks_1(html),get_remarks_2(html),
                get_price(html),get_path(html),get_route(html),
                get_land_space(html),get_build_space(html),get_floor_plan(html),
                get_floor_plan_detail(html),get_build_year(html)
            ]
            write_fp.writerow(csv_output_row)

        #既にページが存在していない時は飛ばす
        except urllib.error.HTTPError:
            pass
