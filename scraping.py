from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

u_url = input("What website would you like to scrape? ")
text = input("What would you like to search for? ")
with urlopen(u_url) as response:
	#indata = response.read()
	soup = BeautifulSoup(response, 'html.parser')
	for line in soup.get_text():
		if text in line:
			#print("true")
			outdata = open('/Users/mitchelking/Python/test.txt', 'ab')
			outdata.write(line)
		else:
			exit()



		
