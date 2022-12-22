import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn import model_selection

df = pd.read_excel('emlakdata.xlsx')


df['fiyat'] = df['fiyat'].str.replace('[TL,\n]','')
df['fiyat'] = df['fiyat'].apply(lambda x: x.replace('.',''))
df['fiyat']=df['fiyat'].astype(int)

df['alan'] = df['alan'].str.replace('\n','')
df['alan'] = df['alan'].str.replace('m2','')
df['alan'] = df['alan'].apply(lambda x: x.replace('.',''))
df['alan']=df['alan'].astype(float)

df2 = df.copy()

df['yas'] = df['yas'].str.replace('Yaşında','')
df['yas'] = df['yas'].str.replace('Sıfır Bina','0')
df['yas'] = df['yas'].str.replace(' ','')
df['yas']=df['yas'].astype(int)

df2.yas = df.yas

for a in range(0, 999, 5):
  b = a + 4
  df['yas'] = df['yas'].replace([df2.yas[df2['yas'].between(a,b)]], str(a)+'-'+str(b)+' Yaşında')

df['konum'] = df['konum'].str.replace('[\n]','')
df['kat'] = df['kat'].str.replace('[\n]','')
df['kat'] = df['kat'].str.replace('                      ','')
df['kat'] = df['kat'].replace(['Yüksek Giriş', 'Giriş Katı', 'Zemin'], 'Giriş')
df['kat'] = df['kat'].str.replace('Yarı Bodrum','Kot 1')
df['kat'] = df['kat'].replace(['Villa Katı'],'Villa')
df['kat'] = df['kat'].str.replace('Ara Kat','3. Kat')
df['kat'] = df['kat'].str.replace('En Üst Kat','5. Kat')
df['kat'] = df['kat'].str.replace('Bodrum ve Zemin','Bodrum')

df.drop(df.index[df['yas'] == '995-999 Yaşında'], inplace = True)
df.drop(df.index[df['yas']=='60-64 Yaşında'], inplace = True)
df.drop(df.index[df['yas']=='50-54 Yaşında'], inplace = True)
df.drop(df.index[df['yas']=='45-49 Yaşında'], inplace = True)

df.drop(df.index[df['fiyat']>3000001], inplace = True)

df.drop(df.index[df['alan']<30], inplace = True)

df.drop(df.index[df['kat']==''], inplace = True)
df.drop(df.index[df['oda']=='365 + 1'], inplace = True)

df.reset_index()

df.to_excel('emlakdatafinal.xlsx')