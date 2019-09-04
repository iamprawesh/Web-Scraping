# div poster =>   a["href"] ==> div[1]class pswp__zoom-wrap =>img[0][src]
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class Film():
	"""docstring for Film"""
	def __init__(self):		
		self.title = ""
		self.link = ""

def get_film_list():
	driver = webdriver.PhantomJS(executable_path=r'C:\Users\DELL-PC\Desktop\scraping\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	
	url = 'https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc'
	
	driver.get(url)
	
	html_doc = driver.page_source
	
	soup = BeautifulSoup(html_doc,'lxml')
	
	film_list = []
	
	divi = soup.find_all('div', class_ = 'lister-item-content')
	
	for div in divi:
		title_desc = div.find("h3" , class_="lister-item-header")
		full_title = title_desc.text.strip().replace("\n","")
		
		a = div.find('a')
		link = "https://www.imdb.com"+a['href']
		
		print(link)
		print(full_title)

		
		new_film = Film()
		new_film.title = full_title
		new_film.link = link
		film_list.append(new_film)

	driver.quit()

	return film_list

def download_all_posters(film_list):
	
	driver = webdriver.PhantomJS(executable_path=r'C:\Users\DELL-PC\Desktop\scraping\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	for film in film_list:

		url = film.link
		driver.get(url)
		print("Above url" +url)
		html_doc = driver.page_source
		soup = BeautifulSoup(html_doc,'lxml')

		div = soup.find('div',class_='poster')
		a = div.find('a')
		url =  'http://www.imdb.com' + a['href']

		driver.get(url)
		print("Below url" +url)
		html_doc = driver.page_source
		soup = BeautifulSoup(html_doc,'lxml')

		all_div = soup.find_all('div',class_="pswp__zoom-wrap")
		all_img = all_div[1].find_all('img')

		print(all_img[1]['src'])
		
		f = open('{1}.jpg'.format(film.title.encode('utf-8').replace(':','')), 'wb')
		f.write(requests.get(all_img[1]['src']).content)
		f.close()

	driver.quit()



download_all_posters( get_film_list() )