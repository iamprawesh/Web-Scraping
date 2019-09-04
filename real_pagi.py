from bs4 import BeautifulSoup
import requests
import csv

page = 1
def get_multiple_page():
    for i in range(page,11):
        url = 'http://quotes.toscrape.com/page/'+str(i)+'/'
        get_data(url)
        # print("page=========================> " + str(i))



def get_data(url_item):

    r = requests.get(url_item)
    soup = BeautifulSoup(r.text ,"lxml")
    
    div = soup.find_all("div", class_="row")[1]
    for x in  div.find_all("div", class_="quote"):
    
        author = x.find("small", class_="author")
        tags = x.find("meta", class_="keywords")
        final_tag =tags['content'].replace(',','|')
        final_author = author.text
        print(final_author)
        print(final_tag)

            
        the_writer.writerow({'Author':final_author,'Tag':final_tag})

    
    # print("Page => ================================================================"+ str(i))
    
    # print(url)
with open('quotes.csv','w',newline="") as f:
    fieldnames= ['Author','Tag']

    the_writer = csv.DictWriter(f,fieldnames=fieldnames)
    
    the_writer.writeheader()
    get_multiple_page()