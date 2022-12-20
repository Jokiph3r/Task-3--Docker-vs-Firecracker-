# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:18:08 2022

@author: Engr-Yasir
"""

import pandas as pd
dataset = pd.read_csv('C:/Users/ab12/Documents/ml-Model/dataset_sdn1.csv')

X = dataset.iloc[:,0:12]
y = dataset.iloc[:,12:13]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)

classifier.fit(X_train, y_train)

import pickle
pickle.dump(classifier,open('C:/Users/ab12/Documents/ml-Model/ml.pkl','wb'))



y_pred = classifier.predict(X_test)


from sklearn.metrics import accuracy_score ,precision_score,recall_score ,f1_score
print('\n       Accuracy is %f Percent' %(accuracy_score(y_test,y_pred)*100))
print('\n       Precision score is %f Percent' %(precision_score(y_test,y_pred)*100))
print('\n       Recall Score is %f Percent' %(recall_score(y_test,y_pred)*100))
print('\n       F1-score is %f Percent' %(f1_score(y_test, y_pred)*100))
            