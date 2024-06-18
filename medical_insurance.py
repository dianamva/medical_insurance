# -*- coding: utf-8 -*-
"""Medical_insurance.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rdiyIu2UMCj1QTpk-QyfZo7bXqYuo6lw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from scipy import stats

df = pd.read_csv('insurance.csv')
df.head()

df.info()

df = df[np.abs(stats.zscore(df['charges'])) < 3]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

plt.figure(figsize=(16,8))
sns.heatmap(df.corr(), annot=True)

plt.figure(figsize =(25, 7))
df.boxplot(rot = 90, widths = 0.6, patch_artist = True)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['age'] = scaler.fit_transform(df[['age']])
df['bmi'] = scaler.fit_transform(df[['bmi']])
df['children'] = scaler.fit_transform(df[['children']])

from sklearn.model_selection import train_test_split

from re import X
X = df.drop('charges', axis = 1)
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

from sklearn.metrics import r2_score
r2=r2_score(y_pred,y_test)
print("r2_score:",r2)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)

y_pred1 = rf.predict(X_test)

from sklearn.metrics import r2_score
r2=r2_score(y_pred1,y_test)
print("r2_score:",r2)

