import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

trds = pd.read_csv("train.csv")
teds = pd.read_csv("test.csv")
trds.drop('0', axis=1, inplace=True)
teds.drop('0', axis=1, inplace=True)

train_X = trds[['1', '2', '3', '4', '5', '6']]
train_y = trds.type
test_X = teds[['1', '2', '3', '4', '5', '6']]
test_y = teds.predict

model = RandomForestClassifier(n_estimators=100,
                               bootstrap=True,
                               max_features='sqrt')
model.fit(train_X, train_y)
prediction = model.predict(test_X)
print(prediction)



