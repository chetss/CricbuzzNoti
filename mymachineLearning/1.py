from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import  train_test_split

iris = datasets.load_iris()

# def myfunction():
#     x = iris['data']
#     y = iris['target']

#     df = pd.DataFrame(x,columns=iris['feature_names'])

#     knn = KNeighborsClassifier(n_neighbors=6)

#     knn.fit(x,y)



# def myfunction2():

#     x = iris['data']
#     y = iris['target']

#     X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=21,stratify=y)

#     knn = KNeighborsClassifier(n_neighbors=20)
#     knn.fit(X_train,y_train)
#     y_pred = knn.predict(X_test)
#     print(y_pred)
#     print(knn.score(X_test,y_test))

# myfunction2()

def myfunction3():
    data = pd.read_csv('./new_births_total_number_estimated.csv',)
    x = data['2015']
    temp = x.values.reshape(-1,1)
    df = pd.DataFrame(temp)
    print(df.head())
    

    
myfunction3()