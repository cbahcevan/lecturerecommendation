from sklearn.tree import  DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import numpy as np
import os

def drawTree(clf):
   tree.export_graphviz(clf.tree_,out_file="n.dot"
   ,feature_names=["math","bus"])
   os.system("dot -T png n.dot -o n.png")

"""
yes:1
no:0

math
bus
ge

"""
frame =  pd.DataFrame([[1,0],[0,1],[1,0]])

target = np.array(["math","bus","math"])

clf = DecisionTreeClassifier(criterion="entropy")

clf.fit(frame,target)

predictionData = []
predictionData.append(input("enter 1 if you like math otherwise zero: "))
predictionData.append(input("enter 1 if you like bus otherwise zero: "))
print clf.predict(predictionData)

drawTree(clf)

