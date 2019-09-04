from selenium import webdriver
from bs4 import BeautifulSoup
class Player():
	def __init__(self):
		self.header= ""
		self.year = ""
		self.rting = ""
driver = webdriver.PhantomJS(executable_path=r'C:\Users\DELL-PC\Desktop\scraping\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc'
driver.get(url)
html_doc = driver.page_source
soup = BeautifulSoup(html_doc,'lxml')
file_name = "Top_50_movie_disc.csv"
f=open(file_name,"w")
headers = (" RANK , MOVIE NAME , MOVIE TYPE , YEAR , MOVIE LENGTH , RATINGS ")
f.write(headers)
divi = soup.find_all('div', class_ = 'lister-item-content')
# print(div)
for div in divi:
	title_desc = div.find("h3" , class_="lister-item-header")
	full_title = title_desc.text.strip().replace("\n","")
	rank = full_title.split('.')[0]
	title = full_title.split('.')[1].split('(')[0]
	dop = full_title.split('(')[1][:-1]
	rating = div.find("div" , class_="ratings-imdb-rating").text.strip()
	runtime = div.find("span", class_="runtime")
	mov_type = div.find("span", class_="genre")
	mov = mov_type.text.strip().replace("\n","").replace(",","|")
	f.write("\n" + rank + "," + title + "," + mov + "," + dop + ","+ runtime.text + "," + rating)
	print("\n")
	print(rank)
	print(title)
	print(mov)
	print(dop)
	print(runtime.text)
	print(rating)
	print("=====================")
print(len(divi))
f.close()
driver.quit()

# print(full_title)

# year = soup('span',class_ = 'lister-item-year text-muted unbold')

# h_span = soup.find('p',string=" Director: ")
	# for sp in h_span.findNextSiblings():
# print(h_span)
# for x in div:
# rating = soup.find('div',class_ = 'ratings-bar')
# rting = rating.div
# year = soup('span',class_ = 'lister-item-year')
# print(rting.text)
# print(year.text)
	# print(header.text)
# print(year.text)


	# file_name = "NBA_Players.csv"
	# f=open(file_name,"w")
	# headers = ("Player Name,Link")
	# f.write(headers)
	# title = div.
	# for a in div.find_all('a'):
	# 	new_player = Player()
	# 	new_player.title = a['title']
	# 	new_player.link = "https://www.nba.com" + a['href']
	# 	player_list.append(new_player)
	# # print(len(a))
	# for one_player in player_list:
	# # 	# f.write(one_player.title + "," +one_player.link + "\n")
	# 	print(one_player.title)
	# 	print(one_player.link)
	# f.close()

# get_player_detail()