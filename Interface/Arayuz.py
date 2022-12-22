from itertools import islice
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Canvas
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from sklearn import model_selection
import xgboost as xgb


##***************************##

dfsehir = ['Kütahya', 'Uşak', 'Afyonkarahisar']
dfsehirnum = ['1', '2', '0']

dfkonum = ['Merkez, Yıldırım Beyazıt Mahallesi', 'Merkez, Servi Mahallesi',
       'Merkez, G. Kemal Mahallesi', 'Simav, Muradınlar Mahallesi',
       'Merkez, Yunusemre Mahallesi', 'Merkez, Fatih Mahallesi',
       'Merkez, 30 Ağustos Mahallesi', 'Tavşanlı, Çırçırçeşme Mahallesi',
       'Tavşanlı, Moymul Mahallesi', 'Merkez, Dumlupınar Mahallesi',
       'Tavşanlı, Yeni Mahallesi', 'Simav, Ahlatlıçeşme Mahallesi',
       'Merkez, Bahçelievler Mahallesi', 'Merkez, Parmakören Mahallesi',
       'Merkez, Meydan Mahallesi', 'Merkez, Pirler Mahallesi',
       'Tavşanlı, Durak Mahallesi', 'Merkez, Maltepe Mahallesi',
       'Merkez, Zafertepe Mahallesi', 'Tavşanlı, Subaşı Mahallesi',
       'Merkez, Alipaşa Mahallesi', 'Merkez, Saray Mahallesi',
       'Merkez, Maruf Mahallesi', 'Merkez, Akkent Mahallesi',
       'Merkez, 75. Yıl Mahallesi', 'Merkez, Gaybiefendi Mahallesi',
       'Gediz, Gazikemal Mahallesi', 'Tavşanlı, Hanımçeşme Mahallesi',
       'Simav, Hacıahmetoğlu Mahallesi', 'Merkez, Cumhuriyet Mahallesi',
       'Merkez, Evliya Çelebi Mahallesi', 'Tavşanlı, Ömerbey Mahallesi',
       'Tavşanlı, Yeniköy Mahallesi', 'Aslanapa, Cumhuriyet Mahallesi',
       'Hisarcık, Karşıyaka Mahallesi', 'Merkez, Ok Meydanı Mahallesi',
       'Merkez, Kemalöz Mahallesi', 'Merkez, Durak Mahallesi',
       'Merkez, Atatürk Mahallesi', 'Merkez, Fevzi Çakmak Mahallesi',
       'Merkez, Ünalan Mahallesi', 'Merkez, Kurtuluş Mahallesi',
       'Karahallı, Boğaz Mahallesi', 'Merkez, Kuyucak Mahallesi',
       'Merkez, Sarayaltı Mahallesi', 'Banaz, Şehitler Mahallesi',
       'Banaz, 31 Ağustos Mahallesi', 'Merkez, Dikilitaş Mahallesi',
       'Merkez, Kurşunluk Mahallesi', 'Merkez, İslice Mahallesi',
       'Banaz, Cumhuriyet Mahallesi', 'Merkez, Özdemir Mahallesi',
       'Merkez, Mehmet Akif Ersoy Mahallesi', 'Merkez, Elmacık Mahallesi',
       'Merkez, Yeşil Karaağaç Mahallesi',
       'Merkez, Ovademirler Mahallesi', 'Merkez, Işık Mahallesi',
       'Merkez, Kocatepe Mahallesi', 'Merkez, Yenice Mahallesi',
       'Merkez, Mareşal Fevzi Çakmak Mahallesi',
       'Merkez, Sülün (Hisar) Mahallesi', 'Merkez, Selçuklu Mahallesi',
       'Merkez, Fakıpaşa Mahallesi', 'Merkez, Ali İhsan Paşa Mahallesi',
       'Merkez, Marulcu Mahallesi', 'Merkez, Erenler Mahallesi',
       'Merkez, Erkmen (Hürriyet) Mahallesi',
       'Merkez, Erkmen (Cumhuriyet) Mahallesi',
       'Merkez, İstiklal Mahallesi', 'Merkez, Hattat Karahisar Mahallesi',
       'Merkez, Dörtyol Mahallesi', 'Merkez, Kanlıca Mahallesi',
       'Merkez, Gazi Mahallesi', 'Sandıklı, Ece Mahallesi',
       'Merkez, Zafer Mahallesi', 'Merkez, Karaman Mahallesi',
       'Merkez, Mecidiye Mahallesi',
       'Merkez, Hoca Ahmet Yesevi Mahallesi',
       'Merkez, Güvenevler Mahallesi', 'Merkez, Sahipata Mahallesi',
       'Merkez, Karşıyaka Mahallesi', 'Merkez, Derviş Paşa Mahallesi',
       'Merkez, Osman Gazi Mahallesi', 'İscehisar, Şirinevler Mahallesi',
       'İhsaniye, Gazlıgöl (Yunus Emre) Mahallesi',
       'Merkez, Nazmi Saatçi Mahallesi', 'Merkez, Eşrefpaşa Mahallesi',
       'Merkez, Ali Çetinkaya Mahallesi', 'Merkez, Dairecep Mahallesi',
       'Bolvadin, Konak Mahallesi', 'Dinar, İncirli Mahallesi',
       'İhsaniye, Yaylabağı (Esentepe) Mahallesi',
       'Bolvadin, Yeni Mahallesi', 'Merkez, Ataköy Mahallesi',
       'Merkez, Kayadibi Mahallesi', 'Merkez, Halımoru Mahallesi',
       'Merkez, Hasan Karaağaç Mahallesi', 'Merkez, Kasımpaşa Mahallesi',
       'Merkez, Hamidiye Mahallesi', 'Merkez, Demirçevre Mahallesi',
       'Merkez, Örnekevler Mahallesi', 'Bolvadin, Kırkgöz Mahallesi',
       'Merkez, Esentepe Mahallesi', 'Başmakçı, Gülistan Mahallesi',
       'Merkez, Yunus Emre Mahallesi', 'Merkez, Akmescit Mahallesi',
       'Merkez, Veysel Karani Mahallesi', 'Merkez, Sümer Mahallesi']
dfkonumnum = [ 85,  77,  40,  96,  84,  38,  12, 103,  99,  27, 101,  94,  21,
        71,  66,  72,  97,  60,  87, 100,  18,  74,  62,  14,  13,  41,
         9,  98,  95,  22,  35, 104, 102,   0,  10,  68,  55,  28,  20,
        39,  90,  57,  11,  59,  75,   3,   1,  26,  58,  91,   2,  89,
        65,  30,  82,  70,  49,  56,  81,  61,  78,  76,  37,  17,  63,
        31,  33,  32,  92,  47,  29,  50,  42,  93,  86,  51,  64,  48,
        43,  73,  52,  25,  69, 107, 105,  67,  36,  16,  23,   5,   8,
       106,   7,  19,  54,  44,  46,  53,  45,  24,  88,   6,  34,   4,
        83,  15,  80,  79]


dfoda = ['3 + 1', '2 + 1', '4 + 1', '1 + 1', '5 + 1', '6 + 1', '5 + 2',
       '2 + 0', '6 + 2', '4 + 2', '2 + 2', '7 + 1', '7 + 2']
dfodanum = [ 4,  2,  5,  0,  7,  9,  8,  1, 10,  6,  3, 11, 12]

dfyas = ['20-24 Yaşında', '25-29 Yaşında', '15-19 Yaşında', '5-9 Yaşında',
       '0-4 Yaşında', '30-34 Yaşında', '10-14 Yaşında', '35-39 Yaşında',
       '40-44 Yaşında']
dfyasnum = [3, 4, 2, 8, 0, 5, 1, 6, 7]

dfkat = ['1. Kat', '5. Kat', 'Kot 1', 'Giriş', '4. Kat', '2. Kat', '3. Kat',
       '6. Kat', 'Villa', '8. Kat', '7. Kat', 'Kot 3', 'Bodrum',
       'Bahçe Katı', 'Kot 2', '10. Kat', '11. Kat']
dfkatnum = [ 0,  6, 13, 12,  5,  3,  4,  7, 16,  9,  8, 15, 11, 10, 14,  1,  2]



##***************************##

model = xgb.XGBRegressor()
model.load_model('model.h5')

##***************************##
pencere = Tk()
pencere.title("Ev Fiyat Tahmini")

pencere.configure(background='#81e6d9')
pencere.geometry("1280x720")
pencere.state("normal")

def mesaj():
    messagebox.messagebox.showinfo(title="Başarılı", message="Seçim Başarılı")

def olumsuz():
    messagebox.messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız")

def sehir_duzen():
    global sehir
    sehir_deger = sehir_kutu.get()
    sehirindex = dfsehir.index(sehir_deger)
    sehir = dfsehirnum[sehirindex]
    print(sehir)


def konum_duzen():
    global konum
    konum_sayi = konum_kutu.get()
    konumindex = dfkonum.index(konum_sayi)
    konum = dfkonumnum[konumindex]
    print(konum)

def alan_duzen():
    global alan
    alan = int(alan_entry.get())
    print(alan)

def oda_duzen():
    global oda
    oda_sayi = oda_kutu.get()
    odaindex = dfoda.index(oda_sayi)
    oda = dfodanum[odaindex]
    print(oda)

def yas_duzen():
    global yas
    yas_sayi = yas_kutu.get()
    yasindex = dfyas.index(yas_sayi)
    yas = dfyasnum[yasindex]
    print(yas)

def kat_duzen():
    global kat
    kat_sayi = kat_kutu.get()
    katindex = dfkat.index(kat_sayi)
    kat = dfkatnum[katindex]
    print(kat)

baslık_label = Label(pencere, text = "EV FİYAT TAHMİNİ", font="helvetica 36",borderwidth=20, padx = 40, pady = 40,
                     background = "#90cdf4")        
baslık_label.place(x = 400 ,y = 20)

sehir_label = Label(text = "Şehir Seçimi", font="helvetica 12",borderwidth=6)
sehir_label.place(x = 100, y = 300)

sehirler = ["Afyonkarahisar","Kütahya","Uşak"]
sehir_kutu = Combobox(pencere, values = sehirler)
sehir_kutu.place(x = 100,y = 350)

sehir_buton = Button(pencere, text = "Seç", command = sehir_duzen, font="helvetica 12",borderwidth=6)
sehir_buton.place(x = 100, y = 400)


konum_label = Label(text = "Konum Seçimi", font="helvetica 12",borderwidth=6)
konum_label.place(x = 300, y = 300)

konumlar = ['Merkez, Yıldırım Beyazıt Mahallesi', 'Merkez, Servi Mahallesi',
       'Merkez, G. Kemal Mahallesi', 'Simav, Muradınlar Mahallesi',
       'Merkez, Yunusemre Mahallesi', 'Merkez, Fatih Mahallesi',
       'Merkez, 30 Ağustos Mahallesi', 'Tavşanlı, Çırçırçeşme Mahallesi',
       'Tavşanlı, Moymul Mahallesi', 'Merkez, Dumlupınar Mahallesi',
       'Tavşanlı, Yeni Mahallesi', 'Simav, Ahlatlıçeşme Mahallesi',
       'Merkez, Bahçelievler Mahallesi', 'Merkez, Parmakören Mahallesi',
       'Merkez, Meydan Mahallesi', 'Merkez, Pirler Mahallesi',
       'Tavşanlı, Durak Mahallesi', 'Merkez, Maltepe Mahallesi',
       'Merkez, Zafertepe Mahallesi', 'Tavşanlı, Subaşı Mahallesi',
       'Merkez, Alipaşa Mahallesi', 'Merkez, Saray Mahallesi',
       'Merkez, Maruf Mahallesi', 'Merkez, Akkent Mahallesi',
       'Merkez, 75. Yıl Mahallesi', 'Merkez, Gaybiefendi Mahallesi',
       'Gediz, Gazikemal Mahallesi', 'Tavşanlı, Hanımçeşme Mahallesi',
       'Simav, Hacıahmetoğlu Mahallesi', 'Merkez, Cumhuriyet Mahallesi',
       'Merkez, Evliya Çelebi Mahallesi', 'Tavşanlı, Ömerbey Mahallesi',
       'Tavşanlı, Yeniköy Mahallesi', 'Aslanapa, Cumhuriyet Mahallesi',
       'Hisarcık, Karşıyaka Mahallesi', 'Merkez, Ok Meydanı Mahallesi',
       'Merkez, Kemalöz Mahallesi', 'Merkez, Durak Mahallesi',
       'Merkez, Atatürk Mahallesi', 'Merkez, Fevzi Çakmak Mahallesi',
       'Merkez, Ünalan Mahallesi', 'Merkez, Kurtuluş Mahallesi',
       'Karahallı, Boğaz Mahallesi', 'Merkez, Kuyucak Mahallesi',
       'Merkez, Sarayaltı Mahallesi', 'Banaz, Şehitler Mahallesi',
       'Banaz, 31 Ağustos Mahallesi', 'Merkez, Dikilitaş Mahallesi',
       'Merkez, Kurşunluk Mahallesi', 'Merkez, İslice Mahallesi',
       'Banaz, Cumhuriyet Mahallesi', 'Merkez, Özdemir Mahallesi',
       'Merkez, Mehmet Akif Ersoy Mahallesi', 'Merkez, Elmacık Mahallesi',
       'Merkez, Yeşil Karaağaç Mahallesi',
       'Merkez, Ovademirler Mahallesi', 'Merkez, Işık Mahallesi',
       'Merkez, Kocatepe Mahallesi', 'Merkez, Yenice Mahallesi',
       'Merkez, Mareşal Fevzi Çakmak Mahallesi',
       'Merkez, Sülün (Hisar) Mahallesi', 'Merkez, Selçuklu Mahallesi',
       'Merkez, Fakıpaşa Mahallesi', 'Merkez, Ali İhsan Paşa Mahallesi',
       'Merkez, Marulcu Mahallesi', 'Merkez, Erenler Mahallesi',
       'Merkez, Erkmen (Hürriyet) Mahallesi',
       'Merkez, Erkmen (Cumhuriyet) Mahallesi',
       'Merkez, İstiklal Mahallesi', 'Merkez, Hattat Karahisar Mahallesi',
       'Merkez, Dörtyol Mahallesi', 'Merkez, Kanlıca Mahallesi',
       'Merkez, Gazi Mahallesi', 'Sandıklı, Ece Mahallesi',
       'Merkez, Zafer Mahallesi', 'Merkez, Karaman Mahallesi',
       'Merkez, Mecidiye Mahallesi',
       'Merkez, Hoca Ahmet Yesevi Mahallesi',
       'Merkez, Güvenevler Mahallesi', 'Merkez, Sahipata Mahallesi',
       'Merkez, Karşıyaka Mahallesi', 'Merkez, Derviş Paşa Mahallesi',
       'Merkez, Osman Gazi Mahallesi', 'İscehisar, Şirinevler Mahallesi',
       'İhsaniye, Gazlıgöl (Yunus Emre) Mahallesi',
       'Merkez, Nazmi Saatçi Mahallesi', 'Merkez, Eşrefpaşa Mahallesi',
       'Merkez, Ali Çetinkaya Mahallesi', 'Merkez, Dairecep Mahallesi',
       'Bolvadin, Konak Mahallesi', 'Dinar, İncirli Mahallesi',
       'İhsaniye, Yaylabağı (Esentepe) Mahallesi',
       'Bolvadin, Yeni Mahallesi', 'Merkez, Ataköy Mahallesi',
       'Merkez, Kayadibi Mahallesi', 'Merkez, Halımoru Mahallesi',
       'Merkez, Hasan Karaağaç Mahallesi', 'Merkez, Kasımpaşa Mahallesi',
       'Merkez, Hamidiye Mahallesi', 'Merkez, Demirçevre Mahallesi',
       'Merkez, Örnekevler Mahallesi', 'Bolvadin, Kırkgöz Mahallesi',
       'Merkez, Esentepe Mahallesi', 'Başmakçı, Gülistan Mahallesi',
       'Merkez, Yunus Emre Mahallesi', 'Merkez, Akmescit Mahallesi',
       'Merkez, Veysel Karani Mahallesi', 'Merkez, Sümer Mahallesi']
konum_kutu = Combobox(pencere, values = konumlar)
konum_kutu.place(x = 300,y = 350)

konum_buton = Button(pencere, text = "Seç", command = konum_duzen, font="helvetica 12",borderwidth=6)
konum_buton.place(x = 300, y = 400)

oda_label = Label(text = "Oda Sayısı Seçiniz", font="helvetica 12",borderwidth=6)
oda_label.place(x = 500, y = 300)

odalar = ['3 + 1', '2 + 1', '4 + 1', '1 + 1', '5 + 1', '6 + 1', '5 + 2',
       '2 + 0', '6 + 2', '4 + 2', '2 + 2', '7 + 1', '7 + 2']
oda_kutu = Combobox(pencere, values = odalar)
oda_kutu.place(x = 500, y = 350)

oda_buton = Button(pencere, text = "Seç", command = oda_duzen, font="helvetica 12",borderwidth=6)
oda_buton.place(x = 500, y = 400)

yaş_label = Label(text = "Bina Yaşını Seçiniz", font="helvetica 12",borderwidth=6)
yaş_label.place(x = 100, y = 500)

yaşlar = ['20-24 Yaşında', '25-29 Yaşında', '15-19 Yaşında', '5-9 Yaşında',
       '0-4 Yaşında', '30-34 Yaşında', '10-14 Yaşında', '35-39 Yaşında',
       '40-44 Yaşında']
yas_kutu = Combobox(pencere, values = yaşlar)
yas_kutu.place(x = 100, y = 550)

yaşlar_buton = Button(pencere, text = "Seç", command = yas_duzen, font="helvetica 12",borderwidth=6)
yaşlar_buton.place(x = 100, y = 600)


alan_label = Label(pencere, text = "Evin Alanını Girin", font="helvetica 12",borderwidth=6)
alan_label.place(x = 300, y = 500)

alan_entry = Entry()
alan_entry.place(x = 300, y = 550)

alan_buton = Button(pencere, text = "Seç", command = alan_duzen, font="helvetica 12",borderwidth=6)
alan_buton.place(x = 300, y = 600)

kat_label = Label(text = "Daire Katını Seçiniz", font="helvetica 12",borderwidth=6)
kat_label.place(x = 500, y = 500)

katlar = ['1. Kat', '5. Kat', 'Kot 1', 'Giriş', '4. Kat', '2. Kat', '3. Kat',
       '6. Kat', 'Villa', '8. Kat', '7. Kat', 'Kot 3', 'Bodrum',
       'Bahçe Katı', 'Kot 2', '10. Kat', '11. Kat']
kat_kutu = Combobox(pencere, values = katlar)
kat_kutu.place(x = 500, y = 550)

kat_buton = Button(pencere, text = "Seç", command = kat_duzen, font="helvetica 12",borderwidth=6)
kat_buton.place(x = 500, y = 600)

def hesapla():
    df = pd.DataFrame(columns=['oda', 'alan', 'kat', 'yas', 'sehir', 'konum'])

    temp = {'oda' : oda,'alan' : alan,'kat' : kat,'yas' : yas,'sehir' : sehir,'konum' : konum}
    
    df = df.append(temp,ignore_index=True)
    df["oda"] = df["oda"].astype(int)
    df["alan"] = df["alan"].astype(int)
    df["kat"] = df["kat"].astype(int)
    df["yas"] = df["yas"].astype(int)
    df["sehir"] = df["sehir"].astype(int)
    df["konum"] = df["konum"].astype(int)
    print(df)
    df.info()
    pred = model.predict(df)
    
    
    if(pred < 0):
        pred = -1*pred
    
    pred = int(pred)
    
    s2 = Label(pencere, text = pred, font="helvetica 12",borderwidth=6, padx =200, pady = 40)
    s2.place(x = 800, y = 600)

hesapla_buton = Button(pencere, text = "HESAPLA", command = hesapla, font="helvetica 15",borderwidth=60, padx = 100, pady = 40, background = "#f7fafc")
hesapla_buton.place(x = 800, y = 300)

s1 = Label(pencere, text= "", font="helvetica 12",borderwidth=6, padx = 200, pady = 40)
s1.place(x = 800, y = 600)

mainloop()