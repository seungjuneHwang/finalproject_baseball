import requests
from bs4 import BeautifulSoup

import json

url = "https://sports.news.naver.com/kbaseball/record/ajaxHtmlPlayerRecord.nhn?category=kbo&year=2023&type=pitcher&playerOrder=era"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
print(response.status_code)
# print(soup.select('#_pitcherRecord'))
# print(soup.text)
dict_example = json.loads(soup.text)
print(type(dict_example))
for i in dict_example:
    print(i['rank'], i['team'], i['name'])
# #_pitcherRecord > table:nth-child(3) > tbody
# for tr_tag in soup.find(id='regularTeamRecordList_table').find_all('tr'):
# for tr_tag in soup.find(id='regularTeamRecordList_table').find_all('tr'):
# for th_tag in soup.select("#_pitcherRecord > table:nth-child(3) > tbody > tr"):
#     name = th_tag.select('td.ply')
#     print(name)
    # th_tag = tr_tag.find('th')
    # strong_tag = th_tag.find('strong')
    # lank = strong_tag.get_text()

    # span_tag = tr_tag.findAll('span')
    # team = span_tag[0].get_text()
    # total = span_tag[1].get_text()
    # win = span_tag[2].get_text()
    # lose = span_tag[3].get_text()
    # draw = span_tag[4].get_text()
    # rate = span_tag[5].get_text()
    # gab = span_tag[6].get_text()
    # contin = span_tag[7].get_text()
    # gobase = span_tag[8].get_text()
    # longhit = span_tag[9].get_text()
    # lately = span_tag[10].get_text()

    # print(lank, " ", team, " ",  total, "| 경기수 :", win, "| 승 :", lose, "| 패 :", draw, "| 무 :", rate, "| 게임차 :", gab, "| 연속 :", contin, "| 출루율 :", gobase, "| 장타율 :", longhit, "| 최근10경기 :", lately)