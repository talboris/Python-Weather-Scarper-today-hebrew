import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import socket
import binascii
import os
import sys
import codecs

def geturls(url):
	r=requests.get(url)
	return requests.get(url)
def main():

	
	
	
	

	url='http://www.ims.gov.il/ims/all_tahazit/'
	r=geturls(url)
	print(geturls(url))
	x=r.status_code
	type(url)
	if type(x) is int:
		print("Check file in the current directory for weather forecast for today , some consoles cant read hebrew ")
	else:
		print("not hello")
	print(x)
	
	if (r.status_code) !=200:
		print('the page not avai')
		
	soup=BeautifulSoup(r.content,'html.parser')
	forecast=soup.find(id="_ctl0_PageBody_HPforecast1_tdDailyForecast").get_text()
	#print(forecast)
	filez=open('forecastfile.txt', 'w+',encoding='utf8')
	filez.write(forecast)
	filez=open('forecastfile.txt', 'r',encoding='utf8')
	data=filez.read()
	print(data)
	
	
	#for item in list(soup.children):
	#print(type(item))

main()


"""
	sys.stdout = codecs.getwriter('utf8')(sys.stdout)
	sys.stderr = codecs.getwriter('utf8')(sys.stderr)
,encoding="utf8"

"""
