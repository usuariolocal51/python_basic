import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

data = {
    '__VIEWSTATE': '',
    '__VIEWSTATEGENERATOR': '',
    '__EVENTVALIDATION': '',
    'ctl00$CPH_Main$TextBox1': '',
    'ctl00$CPH_Main$Button1': 'Search',
    'ctl00$CPH_Main$CheckBox_Contestant': 'on',
    'ctl00$CPH_Main$DropDownListFrom': '1959',
    'ctl00$CPH_Main$DropDownListTo': '2019'
}


def get_results(search_term):
    with requests.Session() as s:
        r = s.get('https://www.imo-official.org/search.aspx')
        soup = bs(r.content, 'lxml')
        d = {i['id']: i['value'] for i in soup.select('[type="hidden"]')}
        for k, v in d.items():
            data[k] = v
        data['ctl00$CPH_Main$TextBox1'] = search_term
        r = s.post('https://www.imo-official.org/search.aspx', data=data)
        soup = bs(r.content, 'lxml')
        df = pd.read_html(str(soup.select('table')[1]))[0]
        return df


print(get_results('Zhuo Qun Song'))
