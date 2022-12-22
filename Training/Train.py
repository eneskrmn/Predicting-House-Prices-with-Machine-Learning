import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn import model_selection
from sklearn import preprocessing

df3 = pd.read_excel("emlakdatafinal.xlsx")
df3.drop("Unnamed: 0", axis = 1, inplace =True)
df = df3.copy()

df = df[["fiyat","oda","alan","kat","yas","sehir", 'konum']]

le = preprocessing.LabelEncoder()
df.fiyat = df3.fiyat
df.oda = le.fit_transform(df3.oda)
df.alan = df3.alan
df.kat = le.fit_transform(df3.kat)
df.yas = le.fit_transform(df3.yas)
df.sehir = le.fit_transform(df3.sehir)
df.konum = le.fit_transform(df3.konum)

r = np.arange(len(df)).repeat(10)
df.iloc[r].reset_index(drop=True)

x = df.drop(["fiyat"], axis =1)
y = df["fiyat"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 144)

params = {"colsample_bytree":[0.4,0.6,0.8], "learning_rate":[0.01,0.02,0.04],"max_depth":[6,7,8],"n_estimators":[400,500,600]}
xgb = XGBRegressor()

grid = GridSearchCV(xgb, params, cv=10, n_jobs = -1, verbose =2)
grid.fit(X_train, y_train)
grid.best_params_

xgb1 = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.07, max_depth = 7, n_estimators = 400)

model_xgb = xgb1.fit(X_train, y_train)

model_xgb.predict(X_test)[5:15]

y_test[5:15]

model_xgb.score(X_test, y_test)

model_xgb.score(X_train, y_train)

model_xgb.save_model('model.h5')

