import re
import requests
from bs4 import BeautifulSoup
import urllib
import json


class scraper:
	
	def __init__(self):
		self.session = requests.Session()
		
		
	def scrapeWebsite(self,url):
		response = self.session.get(url)
		response_text = response.text
		return response_text
		
	def parserHTML(self,text):
		para = []
		soup = BeautifulSoup(text,'html.parser')
		script = soup.findAll('script')
		tag = script[12]
		for x in tag:
			para.append(str(tag))
		para = str(para)
		para = re.findall(r'lrrr_data = {.*}',para)
		para = str(para)
		para = re.findall(r'{.*}',para)
		return para
		
	def writer(self,text,file):
		f = open(file,'w+')
		for l in text:
			f.write(l)
		f.close()