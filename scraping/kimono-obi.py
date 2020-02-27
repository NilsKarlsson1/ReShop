
#  pip3 install requests beautifulsoup4 lxml
import json
import requests
from bs4 import BeautifulSoup


def scrapingKimonoObi():
    
    listelem = []
    
    
    dataHtml = requests.get(site + link).text
    dataParse = BeautifulSoup(dataHtml, "lxml")
    posts = dataParse.findAll("div", {"class": 'product-wrap'})
    for post in posts:
        url = post.find('a', {'class': 'product-info__caption'}).attrs['href']
        listelem.append(url)
    
    for lien in listelem:
        dataHtml = requests.get(site + lien).text
        dataParse = BeautifulSoup(dataHtml, "lxml")
        element = {}



        
        title = dataParse.find('h1', {'class': 'product_name'})
        element['titre'] = title.text

        price = dataParse.find('span',{'class': 'current_price'}).find('span', {'class': 'money'})
        element['prix'] = price.text

        img = dataParse.find('img', {'data-index': '0'}).attrs['src']
        element['img'] = img
        
        description = dataParse.find('div', {'class': 'description bottom'}).text
        element['description'] = description

        stock = dataParse.find('span', {'class': 'sold_out'}).text
        element['dispo'] = stock

        element['lien'] = "https://kimono-obi.com" + lien

        element['tag1'] = tagVendor

        element['tag2'] = tagType

        element['tag3'] = tagSexe

        
        bdd.append(element)
            
    

def saveData(data):
    print("create or update scrapingKimonoObi.json")
    with open('scrapingKimonoObi.json', 'w+', encoding='utf-8') as outfile:
        print("insert all the data scraped")
        json.dump(data, outfile)
        print("done")

    


    

if __name__ == "__main__":
    bdd = []
    site = "https://kimono-obi.com"
    tagVendor = "kimono-obi"
    tagType = "vetement"
    tagSexe = "femme"

    link = "/collections/kimono-femme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/yukata-femme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/kimono-sexy"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/monokini"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/jinbei-femme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/geta-femme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/obi-femme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    tagSexe = "homme"
    
    link = "/collections/kimono-homme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/yukata-homme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/jinbei-homme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/geta-homme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/obi-homme"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    tagSexe = "mixte"

    link = "/collections/veste-japonaise"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/pull-japonais"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/pantalon-streetwear"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/kimono-cardigan"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/tee-shirt-japonais"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/short-streetwear"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    tagType = "accessoire"

    link = "/collections/eventail-japonais"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/casquette-baseball"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/chaussette-japonaise"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/cache-nez"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/bonnet-streetwear"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/eventail-japonais"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    link = "/collections/eventail-japonais"
    scrapingKimonoObi()
    print("scraping "+ site+link+" done")

    
    saveData(bdd)
    print("scraping of KimonoObi successful")





















