import bs4 as bs
from selenium import webdriver
import os
import requests

driver = webdriver.Firefox(executable_path = os.getcwd() + '/geckodriver')

class details : 
    def __init__(self,det):
        self.pts = det[0] 
        self.reb = det[1] 
        self.ast = det[2]
        self.pie = det[3] 
        self.ht =  det[4]
        self.wt =  det[5] 
        self.age = det[6] 
        self.birth = det[7] 
        self.prior = det[8] 
        self.draft = det[9] 
        self.exp =   det[10] 

    def __str__() : 
        return f"""
                 Points : {self.pts}
                 REB    : {self.reb}
                 Assist : {self.ast}
                 PIE    : {self.pie}
                 Height : {self.ht}
                 Weight : {self.wt}
                 Age    : {self.age}
                 DOB    : {self.birth}
                 Prior  : {self.prior}
                 Experience : {self.exp}
                 Draft  : {self.draft}
                 """

class Player : 

    def __init__(self,name, link) :
        self.name = name
        self.link = 'https://stats.nba.com'+link
      
        #Calling getinfo() to fetch the remaining info following the link
        det = self.getInfo(self.link)
        self.detail = details(det)
    
    def getInfo(self,link) : #Obtaining stats of current player
        print(f"Fecthing details for {link}")
        driver.get(link)
        soup = bs.BeautifulSoup(driver.page_source,'lxml')
        stats_list = soup.find_all('div',class_='player-stats__item')
        val = [each_stat.get_text().strip().split('\n')[1] for each_stat in stats_list]
        print("Values : ")
        print(val)
        
        print("Fetching Image",end='\n\n')
        #Fetching Image 
        img = soup.find('img',class_='player-img')
        r = requests.get(img['src'])
        f = open("Player_Images/"+img['alt'] + '.png','wb')
        f.write(r.content)
        f.close()
        return val #List of stat values
if not os.path.exists('Player_Images')  :
    os.makedirs('Player_Images')


main_url = 'https://stats.nba.com/players/list/'
driver.get(main_url)
soup = bs.BeautifulSoup(driver.page_source,'lxml')
#Fetching the sections containing the player names alphabetically ordered
sections = soup.find_all('section', class_='row collapse players-list__section')
divs = [section.find('div',class_='large-10 columns') for section in sections]

Player_obj = []
for a in divs[0].find_all('a')[:10]: 
        print(f"Fetching name and details link for player {a.text}")
        Player_obj.append(Player(a.text, a.get('href'))) 
