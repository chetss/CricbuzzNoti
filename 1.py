from sklearn import datasets
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import  train_test_split
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
# houseing = datasets.load_boston()

# commented fuction

    # def myfunction1():
    #     ''' using train_test_split() '''
    #     # ? feature_name
    #         # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    #     # ? feature data
    #         #                 5.1               3.5                1.4               0.2
    #         #                 4.9               3.0                1.4               0.2
    #         #                 4.7               3.2                1.3               0.2
    #         #                 4.6               3.1                1.5               0.2
    #         #                 5.0               3.6                1.4               0.2
    #     # ?target_name
    #     # 0 for setosa
    #     # 1 for versicolor
    #     # 2 for virginica
    #         # ['setosa' 'versicolor' 'virginica']
    #     # ? target data
    #         #  here we have only 0 for first 5 data which represent setosa
    #         # [0 0 0 0 0 ]
    #         # x is feature data
    #     x = iris['data']
    #     # y is target data
    #     y = iris['target']
    #     # train_test_split() split our data into 4 array 
    #         # X_train contain feature data
    #         # y_train contain target data respective to the feature data (X_train)
    #         # X_test contain feature data for testing the algorithm for testing the algorthim
    #         # y_test contain target data respective to the feature data (x_test) 
    #         #  y_test is used to test the accuracy of the model 
    #     X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=21,stratify=y)
    #     # creating the an instance of knn 
    #     knn = KNeighborsClassifier(n_neighbors=20)
    #     # training a model on the data (training = fitting)
    #     # fit() method takes two argument
    #         # 1. feature data
    #         # 2. target data respective to the feature data 
    #     knn.fit(X_train,y_train)
    #     #  predict the result on the trained model for the given output (argument)
    #     y_pred = knn.predict(X_test)
    #     # checking the accuracy of the our model we pass (X_test,y_test)S
    #     print(knn.score(X_test,y_test))

def my_cross_val_score_demo():
    ''' using cross_val_score() '''
    # ? feature_name
        # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    # ? feature data
        #                 5.1               3.5                1.4               0.2
        #                 4.9               3.0                1.4               0.2
        #                 4.7               3.2                1.3               0.2
        #                 4.6               3.1                1.5               0.2
        #                 5.0               3.6                1.4               0.2
    # ?target_name
    # 0 for setosa
    # 1 for versicolor
    # 2 for virginica
        # ['setosa' 'versicolor' 'virginica']
    # ? target data
        #  here we have only 0 for first 5 data which represent setosa
        # [0 0 0 0 0 ]
        # x is feature data
    X = iris['data']
    # y is target data
    y = iris['target']
    
    knn = KNeighborsClassifier(n_neighbors=20)

    cv_scores = cross_val_score(knn,X,y,cv=5)
    print(cv_scores)
    


# def myfunction2():
#     # in the bostron houseing dataset 
#     #  target_name is "MEDV"
#     #   but you can't access the target_name in this dataset
#     print(houseing.keys())
#     x = houseing['data']
#     df = pd.DataFrame(x,columns=houseing['feature_names'])
#     print(df.head())
#     print(houseing['target'])
    
my_cross_val_score_demo()