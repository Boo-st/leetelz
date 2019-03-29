from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import re
import datetime


class crypto:

	def get_price(var):

		link = (f"https://min-api.cryptocompare.com/data/price?fsym={var}&tsyms=AUD,JPY,EUR")
		req = urllib.request.Request(link, data=None, headers={
							'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
						})
		z = urllib.request.urlopen(req).read().decode()
		return(z)







var = input("What crypto would you like?")
if var.isupper():
	print(crypto.get_price(var))
else:
	var = var.upper()
	print(crypto.get_price(var))

