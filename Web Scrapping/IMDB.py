from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import bs4 as bs
import requests
import pandas as pd
import pickle
class Film : 
    def __init__(self,name, year, link) : 
        self.name = name
        self.year = year[1:-1]
        self.link = link
        self.img_link = None 

    def __str__(self) : 
        return f"""{self.name} released in {self.year} full details --> {self.link}"""
    def get_details(self) : 
        return list([self.name, self.year, self.link])

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options = options, executable_path = os.getcwd() + '/geckdriver')
film = pickle.load(open('films.pkl','rb'))

#Storing in csv file
#films = [each.get_details() for each in film]
#df = pd.DataFrame(films,columns=["Movie Name", "Release Year", "Full Details At"])
#df.to_csv("Top Movies.csv",index=False)
#Stored in csv file

for each in film[:2] : 
    print(f"Working for {each.name}")
    full_poster_name = each.name + ' Poster'

    #Opeining page given in link to fetch the intermediary image link
    driver.get(each.link)
    soup = bs.BeautifulSoup(driver.page_source,'lxml')
    #class=poster-><a href="link"> -------> (Moved to next page)
    intermediary_imgLink  = 'https://www.imdb.com' + soup.find('div',class_='poster').a['href']

    driver.get(intermediary_imgLink)
    #Now this page contains the actual image's link hosted on amazon's servers
    soup = bs.BeautifulSoup(driver.page_source,'lxml')

    each.img_link = soup.find('div',class_='pswp__container').find('img',class_='pswp__img')['src']
    print(each.img_link)

    if not os.path.exists('Posters') : 
        os.makedirs('Posters')
    r = requests.get(each.img_link)
    f = open(os.getcwd() + '/Posters/' + each.name ,'wb')
    f.write(r.content)
    f.close()
   
driver.quit()
