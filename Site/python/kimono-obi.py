
#  pip3 install requests beautifulsoup4 lxml mysql-connector-python
import json
import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  database="mydb"
)

def scrapingKimonoObi(avancement):
    
    listelem = []
    
    
    dataHtml = requests.get(site + link).text
    dataParse = BeautifulSoup(dataHtml, "lxml")
    posts = dataParse.findAll("div", {"class": 'product-wrap'})
    for post in posts:
        url = post.find('a', {'class': 'product-info__caption'}).attrs['href']
        listelem.append(url)

    num = 0 
    for lien in listelem:
        dataHtml = requests.get(site + lien).text
        dataParse = BeautifulSoup(dataHtml, "lxml")
        element = {}

        adding = 1

        
        if dataParse.find('h1', {'class': 'product_name'}) is None:
            adding = 2
        else:
            element['titre'] = dataParse.find('h1', {'class': 'product_name'}).text


        if dataParse.find('span',{'class': 'current_price'}) is None:
            adding = 3
        else:
            element['prix'] = dataParse.find('span',{'class': 'current_price'}).find('span', {'class': 'money'}).text

        if dataParse.find('img', {'data-index': '0'}) is None:
            adding = 4
        else:
            element['img'] = dataParse.find('img', {'data-index': '0'}).attrs['src']

        
        if dataParse.find('div', {'class': 'description bottom'}) is None:
            adding = 5
        else:
            element['description'] = dataParse.find('div', {'class': 'description bottom'}).text


        if dataParse.find('span', {'class': 'sold_out'}) is None:
            adding = 6
        else:
            element['dispo'] = dataParse.find('span', {'class': 'sold_out'}).text


        element['lien'] = "https://kimono-obi.com" + lien

        element['tag1'] = tagVendor

        element['tag2'] = tagType

        element['tag3'] = tagSexe

        if adding == 1:
            num = num + 1
            print("import successfull "+str(num)+"/"+str(len(listelem))+" --> "+str(avancement)+"/23")
            bdd.append(element)
        else:
            print("failed import, code:"+str(adding))
            
    

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
    print("start scraping "+ site+link)
    scrapingKimonoObi(1)
    print("scraping "+ site+link+" done")

    link = "/collections/yukata-femme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(2)
    print("scraping "+ site+link+" done")

    link = "/collections/kimono-sexy"
    print("start scraping "+ site+link)
    scrapingKimonoObi(3)
    print("scraping "+ site+link+" done")

    link = "/collections/monokini"
    print("start scraping "+ site+link)
    scrapingKimonoObi(4)
    print("scraping "+ site+link+" done")

    link = "/collections/jinbei-femme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(5)
    print("scraping "+ site+link+" done")

    link = "/collections/geta-femme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(6)
    print("scraping "+ site+link+" done")

    link = "/collections/obi-femme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(7)
    print("scraping "+ site+link+" done")

    tagSexe = "homme"
    
    link = "/collections/kimono-homme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(8)
    print("scraping "+ site+link+" done")

    link = "/collections/yukata-homme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(9)
    print("scraping "+ site+link+" done")

    link = "/collections/jinbei-homme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(10)
    print("scraping "+ site+link+" done")

    link = "/collections/geta-homme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(11)
    print("scraping "+ site+link+" done")

    link = "/collections/obi-homme"
    print("start scraping "+ site+link)
    scrapingKimonoObi(12)
    print("scraping "+ site+link+" done")

    tagSexe = "mixte"

    link = "/collections/veste-japonaise"
    print("start scraping "+ site+link)
    scrapingKimonoObi(13)
    print("scraping "+ site+link+" done")

    link = "/collections/pull-japonais"
    print("start scraping "+ site+link)
    scrapingKimonoObi(14)
    print("scraping "+ site+link+" done")

    link = "/collections/pantalon-streetwear"
    print("start scraping "+ site+link)
    scrapingKimonoObi(15)
    print("scraping "+ site+link+" done")

    link = "/collections/kimono-cardigan"
    print("start scraping "+ site+link)
    scrapingKimonoObi(16)
    print("scraping "+ site+link+" done")

    link = "/collections/tee-shirt-japonais"
    print("start scraping "+ site+link)
    scrapingKimonoObi(17)
    print("scraping "+ site+link+" done")

    link = "/collections/short-streetwear"
    print("start scraping "+ site+link)
    scrapingKimonoObi(18)
    print("scraping "+ site+link+" done")

    tagType = "accessoire"

    link = "/collections/eventail-japonais"
    print("start scraping "+ site+link)
    scrapingKimonoObi(19)
    print("scraping "+ site+link+" done")

    link = "/collections/casquette-baseball"
    print("start scraping "+ site+link)
    scrapingKimonoObi(20)
    print("scraping "+ site+link+" done")

    link = "/collections/chaussette-japonaise"
    print("start scraping "+ site+link)
    scrapingKimonoObi(21)
    print("scraping "+ site+link+" done")

    link = "/collections/cache-nez"
    print("start scraping "+ site+link)
    scrapingKimonoObi(22)
    print("scraping "+ site+link+" done")

    link = "/collections/bonnet-streetwear"
    print("start scraping "+ site+link)
    scrapingKimonoObi(23)
    print("scraping "+ site+link+" done")
    
    saveData(bdd)
    print("scraping of Kimono-Obi successful")

    with open("scrapingKimonoObi.json") as f:
        file_data = json.load(f)

    mycursor = mydb.cursor()
    sqlinsert = "INSERT INTO `listarticle` (titre, prix, img, description, dispo, lien, tag1, tag2, tag3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE lien = lien"
    for li in file_data:

        val = (li['titre'], li['prix'], li['img'], li['description'], li['dispo'], li['lien'], li['tag1'], li['tag2'], li['tag3'])        

        mycursor.execute(sqlinsert, val)
        mydb.commit()    
        print(mycursor.rowcount, "record inserted.")
    print("insert of DBZ-store successful")


















