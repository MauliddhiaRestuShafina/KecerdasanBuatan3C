# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:18:44 2021

@author: Muh Amri
"""

from sklearn import datasets 
iris = datasets.load_iris()
digits = datasets.load_digits()
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1])
hasil = clf.predict(digits.data[-1:])
print(hasil)

 