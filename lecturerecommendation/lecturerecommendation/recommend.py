<<<<<<< HEAD
from sklearn.tree import  DecisionTreeClassifier
from sklearn import tree
import numpy as np


def evaluate(frame,target,input):
	clf = DecisionTreeClassifier(criterion="entropy")
	print frame
	clf.fit(frame,target)
	return clf.predict(input)
=======
print 'test'
>>>>>>> origin/master
