
#  pip3 install requests beautifulsoup4 lxml
import json
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["listArticle"]
collection_currency = db["article"]


def scrapingDBStrore(avancement):
    
    listelem = []
    
    
    dataHtml = requests.get(site + link).text
    
    dataParse = BeautifulSoup(dataHtml, "lxml")
    posts = dataParse.findAll("a", {"class": 'product-card'})
    for post in posts:
        url = post.attrs['href']
        listelem.append(url)

    num = 0 
    for lien in listelem:
        dataHtml = requests.get(site + lien).text
        
        dataParse = BeautifulSoup(dataHtml, "lxml")
        element = {}

        adding = 1

        
        if dataParse.find('meta', {'itemprop': 'name'}) is None:
            adding = 2
        else:
            element['titre'] = dataParse.find('meta', {'itemprop': 'name'}).attrs['content']


        if dataParse.find('span',{'class': 'money'}) is None:
            adding = 3
        else:
            element['prix'] = dataParse.find('span', {'class': 'money'}).text

        if dataParse.find('a', {'class': 'js-modal-open-product-modal product__photo-wrapper product__photo-wrapper-product-template'}) is None:
            adding = 4
        else:
            element['img'] = dataParse.find('a', {'class': 'js-modal-open-product-modal product__photo-wrapper product__photo-wrapper-product-template'}).attrs['href']

        
        if dataParse.find('div', {'class': 'rte product-single__description'}) is None:
            adding = 5
        else:
            element['description'] = dataParse.find('div', {'class': 'rte product-single__description'}).text


        
        element['dispo'] = ""


        element['lien'] = "https://dbz-store.fr" + lien

        element['tag1'] = tagVendor

        element['tag2'] = tagType

        element['tag3'] = tagSexe

        if adding == 1:
            num = num + 1
            print("import successfull "+str(num)+"/"+str(len(listelem))+" --> "+str(avancement)+"/3")
            bdd.append(element)
        else:
            print("failed import, code:"+str(adding))
            
    

def saveData(data):
    print("create or update dbz-store.json")
    with open('dbz-store.json', 'w+', encoding='utf-8') as outfile:
        print("insert all the data scraped")
        json.dump(data, outfile)
        print("done")

    


    

if __name__ == "__main__":
    bdd = []
    site = "https://dbz-store.fr"
    tagVendor = "dbz-store"
    tagType = "vetement"
    tagSexe = "femme"

    link = "/collections/t-shirt-dragon-ball-z-femme"
    print("start scraping "+ site+link)
    scrapingDBStrore(1)
    print("scraping "+ site+link+" done")

    tagSexe = "dragon ball"
    tagType = "figurine"
    link = "/collections/figurine-dbz"
    print("start scraping "+ site+link)
    scrapingDBStrore(2)
    print("scraping "+ site+link+" done")

    
    tagType = "accessoire"
    link = "/collections/accessoire-dragon-ball-z"
    print("start scraping "+ site+link)
    scrapingDBStrore(3)
    print("scraping "+ site+link+" done")

    
    
    saveData(bdd)
    print("scraping of DBZ-store successful")

    with open("dbz-store.json") as f:
        file_data = json.load(f)

    for li in file_data:
        if collection_currency.find({'lien':li['lien']}) is not None:
             collection_currency.find_one_and_delete({'lien':li['lien']})
        collection_currency.insert_one(li)            
    client.close()



















