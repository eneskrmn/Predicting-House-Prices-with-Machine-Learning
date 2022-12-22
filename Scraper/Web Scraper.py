import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


emlak = pd.DataFrame(columns=['fiyat','oda','alan','kat','yas','sehir','konum'])

a = b = c = d = e = f = g = 0



x = ('https://www.hepsiemlak.com/kutahya-satilik?page=')
for page in range(0,7):
    url = requests.get(x +str(page) + '/')
    
    soup =BeautifulSoup(url.content,'html.parser')
    
    for fiyat in soup.find_all('div',attrs={'class':'list-view-price'}):
        print(fiyat.text)
        emlak=emlak.append({'fiyat':fiyat.text},ignore_index=True)
    
    for oda in soup.find_all('span',attrs={'class':'celly houseRoomCount'}):
        print(oda.text)
        emlak['oda'][a]=oda.text
        a=a+1
    
    for alan in soup.find_all('span',attrs={'class':'celly squareMeter list-view-size'}):
        print(alan.text)
        emlak['alan'][b]=alan.text
        b=b+1
    
    for kat in soup.find_all('span',attrs={'class':'celly floortype'}):
        print(kat.text)
        emlak['kat'][c]=kat.text
        c=c+1
    
    for yas in soup.find_all('span',attrs={'class':'celly buildingAge'}):
        print(yas.text)
        emlak['yas'][d]=yas.text
        emlak['sehir'][d]='Kütahya'
        d=d+1
    
    for konum in soup.find_all('div',attrs={'class':'list-view-location'}):
        print(konum.text)
        emlak['konum'][e]=konum.text
        e=e+1
        
y = ('https://www.hepsiemlak.com/usak-satilik?page=')
for page in range(0,6):
    url = requests.get(y +str(page) + '/')
    
    soup =BeautifulSoup(url.content,'html.parser')
    
    for fiyat in soup.find_all('div',attrs={'class':'list-view-price'}):
        print(fiyat.text)
        emlak=emlak.append({'fiyat':fiyat.text},ignore_index=True)
    
    for oda in soup.find_all('span',attrs={'class':'celly houseRoomCount'}):
        print(oda.text)
        emlak['oda'][a]=oda.text
        a=a+1
    
    for alan in soup.find_all('span',attrs={'class':'celly squareMeter list-view-size'}):
        print(alan.text)
        emlak['alan'][b]=alan.text
        b=b+1
    
    for kat in soup.find_all('span',attrs={'class':'celly floortype'}):
        print(kat.text)
        emlak['kat'][c]=kat.text
        c=c+1
    
    for yas in soup.find_all('span',attrs={'class':'celly buildingAge'}):
        print(yas.text)
        emlak['yas'][d]=yas.text
        emlak['sehir'][d]='Uşak'
        d=d+1
    
    for konum in soup.find_all('div',attrs={'class':'list-view-location'}):
        print(konum.text)
        emlak['konum'][e]=konum.text
        e=e+1

z = ('https://www.hepsiemlak.com/afyonkarahisar-satilik?page=')
for page in range(0,13):
    url = requests.get(z +str(page) + '/')
    
    soup =BeautifulSoup(url.content,'html.parser')
    
    for fiyat in soup.find_all('div',attrs={'class':'list-view-price'}):
        print(fiyat.text)
        emlak=emlak.append({'fiyat':fiyat.text},ignore_index=True)
    
    for oda in soup.find_all('span',attrs={'class':'celly houseRoomCount'}):
        print(oda.text)
        emlak['oda'][a]=oda.text
        a=a+1
    
    for alan in soup.find_all('span',attrs={'class':'celly squareMeter list-view-size'}):
        print(alan.text)
        emlak['alan'][b]=alan.text
        b=b+1
    
    for kat in soup.find_all('span',attrs={'class':'celly floortype'}):
        print(kat.text)
        emlak['kat'][c]=kat.text
        c=c+1
    
    for yas in soup.find_all('span',attrs={'class':'celly buildingAge'}):
        print(yas.text)
        emlak['yas'][d]=yas.text
        emlak['sehir'][d]='Afyonkarahisar'
        d=d+1
    
    for konum in soup.find_all('div',attrs={'class':'list-view-location'}):
        print(konum.text)
        emlak['konum'][e]=konum.text
        e=e+1

print(emlak)
emlak.to_excel('emlakdata.xlsx')