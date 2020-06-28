import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_content(url):
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers)
    content = html.text
    soup = BeautifulSoup(content,'html.parser')
    return soup

def analysis(soup):
# 返回第一个找到的tslb_b
    temp = soup.find('div', class_='tslb_b')
    tr_list = temp.find_all("tr")
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['idesc'],temp['problem'],temp['datetime'],temp['status'] = \
                td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            df = df.append(temp,ignore_index=True)
    return df

num = 10
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for n in range(num):
    url = base_url + str(n+1) + '.shtml'
    soup = get_content(url)
    df = analysis(soup)
    result = result.append(df, ignore_index=False)
result.to_csv('result_csv628.csv')