from bs4 import BeautifulSoup
import requests

def get_links():
    url = "https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm"
    r = requests.get(url)
    soup = BeautifulSoup(r.text ,"lxml")
    for so in soup.find_all("td",class_="titleColumn"):
        links = so.find('a')
        link = "https://www.imdb.com" + links['href']
        # link = links.a['href']
        # print(link)
        get_data(link)

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text ,"lxml")
    div = soup.find_all("div",class_="title_wrapper")
    print(div[0].h1.text)
    # print(link)
get_links()