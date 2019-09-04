from selenium import webdriver
from bs4 import BeautifulSoup
class Book():
	def __init__(self):
		self.title=""
		self.author=""
		# self.=""
		self.title=""

def create_phantom_driver():
	driver = webdriver.PhantomJS(executable_path=r'C:\Users\DELL-PC\Desktop\scraping\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	return driver


link_list_one_page = []
driver = create_phantom_driver()
url ="https://www.amazon.com/s?k=python+programming&crid=1MNJ6XXZ64B5E&sprefix=Python+%2Caps%2C-1&ref=nb_sb_noss_2"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

divs = soup.find_all('div', class_ = 'a-section a-spacing-medium')
for div in divs:
	title = div.find('span', class_ = 'a-size-medium a-color-base a-text-normal')
	final_title  = title.text
	author = div.find_all('span', class_ = 'a-size-base a-link-normal')
	# author = div.find_all('a', class_ = 'a-size-base a-link-normal')
	# final_author = author[0].text.strip()
	price = div.find_all('span', class_ = 'a-offscreen')
	final_price = price[0].text
	rating = div.find('span', class_ = 'a-icon-alt')
	final_rating = rating.text[0:4]
	# print(final_author)
	# print(title.text)
	print(final_title)
	print(final_price)
	print(final_rating)
driver.quit()
# get_download_link_one_page("https://www.amazon.com/s?k=python+programming&crid=1MNJ6XXZ64B5E&sprefix=Python+%2Caps%2C-1&ref=nb_sb_noss_2")
