
#  pip3 install requests beautifulsoup4 lxml
import json
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["listArticle"]
collection_currency = db["article"]


def scrapingShin(avancement):
    
    listelem = []
    
    
    dataHtml = requests.get(site + link).text
    
    dataParse = BeautifulSoup(dataHtml, "lxml")
    posts = dataParse.findAll("a", {"class": 'thumbnail product-thumbnail'})
    for post in posts:
        url = post.attrs['href']
        listelem.append(url)

    num = 0 
    for lien in listelem:
        dataHtml = requests.get(lien).text
        
        dataParse = BeautifulSoup(dataHtml, "lxml")
        element = {}

        adding = 1

        
        if dataParse.find('h1', {'class': 'h1 product-title'}) is None:
            adding = 2
        else:
            element['titre'] = dataParse.find('h1', {'class': 'h1 product-title'}).text


        if dataParse.find('div',{'class': 'current-price'}) is None:
            adding = 3
        else:
            element['prix'] = dataParse.find('div', {'class': 'current-price'}).text

        if dataParse.find('img', {'class': 'js-qv-product-cover'}) is None:
            adding = 4
        else:
            element['img'] = dataParse.find('img', {'class': 'js-qv-product-cover'}).attrs['src']

        
        if dataParse.find('div', {'itemprop': 'description'}) is None:
            adding = 5
        else:
            element['description'] = dataParse.find('div', {'itemprop': 'description'}).text


        
        element['dispo'] = ""


        element['lien'] = lien

        element['tag1'] = tagVendor

        element['tag2'] = tagType

        element['tag3'] = tagSexe

        if adding == 1:
            num = num + 1
            print("import successfull "+str(num)+"/"+str(len(listelem))+" --> "+str(avancement)+"/8")
            bdd.append(element)
        else:
            print("failed import, code:"+str(adding))
            
    

def saveData(data):
    print("create or update ShinSekai.json")
    with open('ShinSekai.json', 'w+', encoding='utf-8') as outfile:
        print("insert all the data scraped")
        json.dump(data, outfile)
        print("done")

    


    

if __name__ == "__main__":
    bdd = []
    site = "https://www.shin-sekai.fr"
    tagVendor = "shin-sekai"
    tagType = "figurine"
    tagSexe = "all"

    link = "/8-figurines"
    print("start scraping "+ site+link)
    scrapingShin(1)
    print("scraping "+ site+link+" done")


    
    link = "/8-figurines?page=2"
    print("start scraping "+ site+link)
    scrapingShin(2)
    print("scraping "+ site+link+" done")

    
    link = "/8-figurines?page=3"
    print("start scraping "+ site+link)
    scrapingShin(3)
    print("scraping "+ site+link+" done")

    link = "/8-figurines?page=4"
    print("start scraping "+ site+link)
    scrapingShin(4)
    print("scraping "+ site+link+" done")

    link = "/8-figurines?page=5"
    print("start scraping "+ site+link)
    scrapingShin(5)
    print("scraping "+ site+link+" done")

    link = "/8-figurines?page=6"
    print("start scraping "+ site+link)
    scrapingShin(6)
    print("scraping "+ site+link+" done")

    link = "/8-figurines?page=7"
    print("start scraping "+ site+link)
    scrapingShin(7)
    print("scraping "+ site+link+" done")

    link = "/8-figurines?page=8"
    print("start scraping "+ site+link)
    scrapingShin(8)
    print("scraping "+ site+link+" done")
    
    saveData(bdd)
    print("scraping of ShinSekai successful")

    with open("ShinSekai.json") as f:
        file_data = json.load(f)

    for li in file_data:
        if collection_currency.find({'lien':li['lien']}) is not None:
             collection_currency.find_one_and_delete({'lien':li['lien']})
        collection_currency.insert_one(li)            
    client.close()



















