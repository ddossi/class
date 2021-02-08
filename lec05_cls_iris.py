#Module Name : lec05_cls_iris.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# df = pd.read_csv("")
dataset = load_iris()
#dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
print(dataset.keys())
print(dataset.data[:5])
print(dataset.target)
print(dataset.target_names)
print(dataset.feature_names)

col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df = pd.DataFrame(data=dataset.data, columns=col_name)
print(df.shape)
print(df.info())
print(df.head())

df["target"] = dataset.target
print(df.shape)
print(df.info())
print(df.tail())


# df["uid"]
# iloc[행idx,렬idx]
# iloc[s:e , s:e]
# iloc[행idx, s:e]

# 문제 = df.iloc[:,:-1]   #처음부터 <=i<맨끝
# 답안 = df.iloc[:,-1]
문제 = df.drop("target", axis=1)
답안 = df["target"]

print(문제[:2])
print(답안[:2])

#*arrays,  test_size=None,train_size=None,   random_state=None,shuffle=True
#X_train, X_test,     y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# #X_train, X_test,  y_train, y_test
문제_학습80, 문제_테스트20, 답안_학습80, 답안_테스트20 \
    = train_test_split(문제, 답안, test_size=0.2, random_state=121, shuffle=True)

# ??모델
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

dt_model = DecisionTreeClassifier()
knn_model = KNeighborsClassifier()
rf_model = RandomForestClassifier()

models = [dt_model, knn_model, rf_model]
for model in models :
    # fit : 학습하다
    model.fit(문제_학습80, 답안_학습80)
    # predict : 시험
    예측답안20 = model.predict(문제_테스트20)
    # score : 예측 정확도 확인
    score = accuracy_score(답안_테스트20, 예측답안20)
    print(model.__class__)
    print(model.__str__(), ":" , score) #0.9666666666666667










