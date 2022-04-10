import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('C:\\Users\\User\\data-sci\\rsf_CPN_2013_2014')
X = df[::][['Kp',  'R', 'Dst', 'ap', 'F107']]
# X = df[::][['R', 'Dst', 'F107']]
# X = df[::][['R', 'F107']]
y = df['RSF']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

score = knn.score(X_test, y_test)
print('accuracy: '+ format(score, '.3%'))