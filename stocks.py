from bs4 import BeautifulSoup
import urllib.request
file = ("")
file1 = ("")


with open(file1, 'r') as infile:
	data = infile.readlines()
	Stock1 = data[0]
	Stock2 = data[1]
	#stock3 = data[2]
	#stock4 = data[3]
		
		
	infile.close()
	
#S1 = ("https://www.google.com.au/search?rlz=1C1GGRV_enAU758AU758&ei=D-UTWtmQEMK40AS_jqboBA&q=asx%3Aqfy&oq=asx%3Aqfy&gs_l=psy-ab.3...7155.123011.0.123089.4.4.0.0.0.0.216.216.2-1.1.0....0...1c.1.64.psy-ab..3.1.216...0j35i39k1j0i67k1j0i131k1.0.lKFysImVfOQ")
def stocks1(S1):
	with open(file, 'a') as ofile:
		req = urllib.request.Request(S1, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
			
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, 'html.parser')
		predata = soup.find('div', {'class': ['_FOc','_Rnb fmob_pr fac-l']})
		predata1 = soup.find('div', {'class': 'vk_gy _KNe vk_h'})
		data = predata.text.strip()
		data1 = predata1.text.strip()
		ofile.write(data1+' ' +data)
		ofile.close()
		
stocks1(Stock1)

#S2 = ("https://www.google.com.au/search?rlz=1C1GGRV_enAU758AU758&ei=LeMcWs7BD4GE8gXG4JDQBg&q=asx%3Abud&oq=asx%3Abud&gs_l=psy-ab.3..35i39k1l2j0i131i67k1j0i67k1j0i131k1l3j0l3.2967571.2968874.0.2969055.6.6.0.0.0.0.331.331.3-1.1.0....0...1c.1.64.psy-ab..5.1.331....0.mQ7ipr_Qkdc")
def stocks2(S2):
	with open(file, 'a') as ofile:
		req = urllib.request.Request(S2, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
			
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, 'html.parser')
		data = soup.find('div', {'class': ['_FOc','_Rnb fmob_pr fac-l']})
		data1 = data.text.strip()
		ofile.write('\n'+"Buddy FPO "+data1)
		ofile.close()
						
stocks2(Stock2)


