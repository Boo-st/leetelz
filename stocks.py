from bs4 import BeautifulSoup
import urllib.request
file = ("")
S1 = ("https://www.google.com.au/search?rlz=1C1GGRV_enAU758AU758&ei=D-UTWtmQEMK40AS_jqboBA&q=asx%3Aqfy&oq=asx%3Aqfy&gs_l=psy-ab.3...7155.123011.0.123089.4.4.0.0.0.0.216.216.2-1.1.0....0...1c.1.64.psy-ab..3.1.216...0j35i39k1j0i67k1j0i131k1.0.lKFysImVfOQ")
def stocks(S1):
	with open(file, 'ab') as ofile:
		req = urllib.request.Request(S1, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
			
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, 'html.parser')
		data = soup.find('div', {'class': '_FOc'})
		data1 = data.find('span', {'class': '_Rnb fmob_pr fac-l'})
		data2 = data1.text.strip().encode()
		#print(data2)
		ofile.write(data2)
		ofile.close()
		
stocks(S1)
