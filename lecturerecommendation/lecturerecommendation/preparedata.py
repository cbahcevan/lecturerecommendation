"""

This part will provide code for sklearn module from database
and user
"""

import pandas as pd
from models import TrainData
import numpy as np


def fitDataToPandas():
	data = []
	for element in TrainData.objects.all():
		current = []
		for feature in  element:
			current.append(feature)
		data.append(current)
	print data

def createTargetForEvaluate(arr):
	return np.array(arr)



fitDataToPandas()


