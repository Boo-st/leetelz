from bs4 import BeautifulSoup
import urllib.request
usa = ("http://www.foxnews.com")
def USA(url):
	url = ("http://www.foxnews.com")
	req = urllib.request.Request(url, data=None, 
    	headers={
        	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})
	z = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(z, 'html.parser')
	#data = soup.find('h3', span = {'cd__headline-text'})
	#headline = soup.find('span',{'class': 'cd__headline-text'})
	#headline1 = headline.find("strong")
	#strip = data.text.strip()
	#print(strip)

#//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/article[1]/div/div[2]/h3/a/span[1]/strong/text()
swiss = ("https://www.swissinfo.ch/eng/latest-news")
def switzlerand(url):
	url = ("https://www.swissinfo.ch/eng/latest-news")
	req = urllib.request.Request(url, data=None, 
    	headers={
        	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})
	z = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(z, "html.parser")

	data = soup.find('span', {'itemprop': 'name headline'})
	strip = data.text.strip()
	print(strip)


aus = ("http://www.news.com.au")
def aus(url):
	url = ("http://www.news.com.au")
	req = urllib.request.Request(url, data=None, 
    	headers={
        	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})

	z = urllib.request.urlopen(req).read()	
	soup = ICantBelieveItsBeautifulSoup(z, "html.parser")

	data = soup.find('h4', {'class': 'heading'})
	strip = data.text.strip()
	#return(strip)
	print(strip)

switzlerand(swiss)
USA(usa)
aus(aus)