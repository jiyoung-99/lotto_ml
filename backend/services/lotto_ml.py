import pandas as pd
import ctypes
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.linear_model import LinearRegression
import numpy as np

def lotto_ml(lotto_list):
    lotto_list = lotto_list
    train = lotto_list
    trainX = []
    trainy = []
    lr = LinearRegression()
    y_predict = 0
    for index, one in enumerate(train):
        
        if(index<80):
            trainX_one = train[index:index+20]
            trainy_one = train[index+20]
            trainX.append(trainX_one)
            trainy.append(trainy_one)
            # lr.fit([trainX_one], trainy_one)
        # elif(index == 99):
        #     print("debug.......3")
        #     # y_predict = lr.predict([trainX_one])
        #     print("debug.......4")
        else:
            trainX_one = train[index-20:index]
            trainy_one = train[index]
            trainX.append(trainX_one)
            trainy.append(trainy_one)
            # lr.fit([trainX_one], trainy_one)
        

        
    trainX_1 = pd.DataFrame(trainX[:-1])
    trainy_1 = pd.DataFrame(trainy[:-1])
    # print("trainX_1", trainX_1)
    # print("trainy_1", trainy_1)
    reg = lr.fit(trainX_1, trainy_1) 
    # print('reg.score(X, y)',reg.score(trainX_1, trainy_1))
    # print("reg.coef_", reg.coef_)
    # print("debug.......", trainX[-1])
    trainX_2 = pd.DataFrame(trainX[-1:])
    y_predict = reg.predict(trainX_2)
    # print("y_predict : ", y_predict)
    # y_predict  = lr.predict([trainX[-1]])
    # print('y_predict : ', y_predict)
    return y_predict