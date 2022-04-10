import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('D:\\ปี4 เทอม 2\\Embed\\Data\\rsf_CPN_2013_2014.csv')

features = df[['Kp', 'R', 'Dst', 'ap', 'F107']]
label = df['RSF']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(features, label)

predict = knn.predict([[0, 68, -32, 0, 113.9], [1.3, 68, -26, 5, 113.9]])
# Yes, Yes, Yes, Yes
print(predict[0])
print(predict[1])



X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.25, random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

score = knn.score(X_test, y_test)
print('accuracy: '+ format(score, '.3%'))
