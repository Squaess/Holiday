# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 18:05:42 2017

@author: Aed
"""

from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[160,0]])