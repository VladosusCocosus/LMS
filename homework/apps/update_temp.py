from bs4 import BeautifulSoup
import urllib.request

def yandex_pogoda():
    weater = []
    html_yandex = urllib.request.urlopen('https://yandex.ru/pogoda/surgut?lat=61.247442&lon=73.416247')
    soup = BeautifulSoup(html_yandex, 'html.parser').find('div', class_='temp fact__temp fact__temp_size_s')
    for span in soup:
        weater.append(span.text)
    return weater

 
def get_act_data():
    act = []
    html_actirovki = urllib.request.urlopen('https://sitv.ru/actirovka/')
    actirovki = BeautifulSoup(html_actirovki, 'html.parser').find('div', class_='activ').find_all('p')
    for i in actirovki:
        act.append(i.text)
    return(act)