from bs4 import BeautifulSoup
import urllib.request
file = ("/Users/mitchelking/Documents/NewsHeadlines/news.txt")

def USA(url):
	with open(file, 'ab') as outfile:

		url = ("http://www.foxnews.com")
		req = urllib.request.Request(url, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, 'html.parser')
		data = soup.find('main', {'class': 'main-content'})
		data1 = data.h2.a
		#headline = soup.find('span',{'class': 'cd__headline-text'})
		#headline1 = headline.find("strong")
		strip = data1.text.strip()
		outfile.write(strip + '/n')
		


def switzlerand(url):
	with open(file, 'ab') as outfile:
	
		url = ("https://www.swissinfo.ch/eng/latest-news")
		req = urllib.request.Request(url, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, "html.parser")

		data = soup.find('span', {'itemprop': 'name headline'})
		strip = data.text.strip()
		outfile.write(strip + '/n')


def aus(url):
	with open(file, 'ab') as outfile:
	
		url = ("http://www.news.com.au")
		req = urllib.request.Request(url, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
		z = urllib.request.urlopen(req).read()	
		soup = BeautifulSoup(z, "html.parser")
		data = soup.find('h4', {'class': 'heading'})
		strip = data.text.strip()
		outfile.write(strip + '/n')
	
switzlerand('https://www.swissinfo.ch/eng/latest-news')
USA('http://www.foxnews.com')
aus('http://www.news.com.au')

