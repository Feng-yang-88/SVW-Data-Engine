#车辆投诉爬虫代码

import pandas as pd
import requests
from bs4 import BeautifulSoup

#根据网址得到soup内容
def get_soup(url):
    html = requests.get(url)
    content = html.text
    soup = BeautifulSoup(content,'html.parser')
    return soup

#根据soup抓取当页表格内容
def analysis(soup):
    
    temp = soup.find('div',class_= 'tslb_b')
    df = pd.DataFrame(columns = ['id','brand', 'car_model','type','desc','problem','datatime','status'])
    tr_list = temp.find_all('tr')
    temp1 ={}
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list)>0:
            
            temp1['id'],temp1['brand'], temp1['car_model'],temp1['type'],temp1['desc'],temp1['problem'],temp1['datatime'],temp1['status']= td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4],td_list[5].text,td_list[6].text,td_list[7].text
            df = df.append(temp1,ignore_index=True)

    return df

#抓取20页表格内容，输出csv文件

page_num = 20
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
result = pd.DataFrame(columns = ['id','brand', 'car_model','type','desc','problem','datatime','status'])

for i in range(page_num):
    
    request_url = f"{base_url}{i+1}.shtml"
    soup = get_soup(request_url)
    df = analysis(soup)
    #print(df)
    result = result.append(df)

result.to_csv('L2_CAR.csv', index = False)