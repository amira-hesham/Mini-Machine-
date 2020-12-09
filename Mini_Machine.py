import pandas as pd
import numpy as np 
import xlrd 
data=pd.read_excel('Insurance.xls')
print(data)
x=data.iloc[:,0].values      # Assign your Feature to X 
y=data.iloc[:,1].values   

# Assign your Label to Y 
print('Features Shape ', x.shape , 'Features Type',type(x))   # Do you remember The Method  
print('labels Shape ', y.shape , 'labels Type', type(y))      # .shape and the Built in Function type()
x
def TrainTestSplitter(X,y, split_ratio):
    key=int((1-split_ratio)*len(X))#80% train and 20% test
    print(key," key")
    X_train=X[:key]    # Training Features 
    X_test=X[key:]     # Testing Features 
    y_train=y[:key]   # Training Labels
    y_test=y[key:]      # Testing Labels
    return X_train, X_test , y_train ,y_test 
#split_ratio from Zero to One 
X_train, X_test , y_train ,y_test =TrainTestSplitter(x,y, 0.2)
print(X_train)
print(X_test)
print('Training Features Shape ', X_train.shape , 'Training Features Type',type(X_train))     
print('Training labels Shape ',  X_test.shape , 'Training labels Type', type( X_test)) 
print('Testing Features Shape ', y_train.shape , 'Testing Features Type',type(y_train))     
print('Testing labels Shape ', y_test.shape , 'Testing labels Type', type(y_test))           
