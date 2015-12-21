"""

This part will provide code for sklearn module from database
and user
"""

import pandas as pd
import numpy as np




def fitDataToPandas(input):
	output = []
	target = []
	for element in input:
		current=[]
		
		current = [element.math,element.lit,
		                                 element.read,element.high,element.music
		                                 ,element.polits]
		target.append(element.lecpref)
		output.append(current)
    
	return (target,output)
		











