import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta

class reader:

	def __init__(self):
		self.GBP_USD = []
		self.USD_GBP = []
		self.TIME = []

	def readFile(self,json):
		df = pd.read_json(json)
		df = df[['GBP_USD','USD_GBP']]
		df = df.iloc[0:1]
		return df

	def createData(self,df):
		if len(self.GBP_USD) < 100:
			self.GBP_USD.append(float(df.iloc[:,0]))
		else:
			self.GBP_USD.pop(0)

		if len(self.USD_GBP) < 100:
			self.USD_GBP.append(float(df.iloc[:,1]))
		else:
			self.USD_GBP.pop(0)

		if len(self.TIME) < 100:
			self.TIME.append(time.strftime('%H:%M:%S', time.gmtime()))
		else:
			self.TIME.pop(0)

		data = {'GBP_USD':self.GBP_USD, 'USD_GBP':self.USD_GBP,'TIME':self.TIME}
		newDF = pd.DataFrame(data)
		return newDF
