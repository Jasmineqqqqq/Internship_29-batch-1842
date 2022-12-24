import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


link='https://www.flipkart.com/search?q=oneplus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=oneplus+mobile%7CMobiles&requestId=eb646d44-b700-4e97-824e-946728f8ccdf&as-searchtext=onepl'

page = requests.get(link)
soup = bs(page.content, 'html.parser')
name=soup.find('div',class_="_4rR01T")
rating=soup.find('div',class_="_3LWZlK")
specification=soup.find('div',class_="fMghEO")

products=[]             
prices=[]               
ratings=[]              
apps = []               
os = []                 
hd = []                 
sound = [] 


# for each in specification:
#     spec=each.find_all('li',class_='rgWa7D')
#     print(spec[0].text)
#     print(spec[1].text)
#     print(spec[2].text)
#     print(spec[4].text)
#     print(spec[5].text)
#     print(spec[7].text)


price=soup.find('div',class_='_30jeq3 _1_WHN1')

for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        
        for each in specification:
            col=each.find_all('li', attrs={'class':'rgWa7D'})
            app =col[0].text
            os_ = col[1].text
            hd_ = col[2].text
            sound_ = col[3].text
            products.append(names.text) 
            prices.append(price.text) 
            apps.append(app)
            os.append(os_) 
            hd.append(hd_) 
            sound.append(sound_) 
            ratings.append(rating.text)   


df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
print(df.head(10))