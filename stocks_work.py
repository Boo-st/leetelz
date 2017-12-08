from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
from operator import itemgetter
import re
file = ("C:\Scratch\Python Scripts\Copy1.txt")
file1 = ("C:\Scratch\Python Scripts\copy2.txt")
file2 = ("C:\Scratch\Python Scripts\graph.txt")
Sname = ("Quantify")

with open(file1, 'r') as infile:
	data = infile.readlines()
	if line[0, 10] True:
		Stock1 = data[0]
	Stock2 = data[1]
	Stock3 = data[2]
	#Stock4 = data[3]
		
		
	infile.close()
	
def graph():
	with open(file, 'r') as ingraph:
		data = ingraph.readlines()
		for line in data:
			if "Quantify" in line:
				search = re.findall("\d+\.\d+", line)
				with open(file2, 'a') as outgraph:
					#outgraph.write(search[0]+"\n")
					lst = [item[0] for item in search]
					#plt.plot(search[0])
					#plt.show()
					for list in search:
						#outgraph.write(list+"\n")												
						ingraph.close()				
						#print(list)
graph()
	
def stocks1(S1):
	with open(file, 'a') as ofile:
		req = urllib.request.Request(S1, data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			})
			
		z = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(z, 'html.parser')
		predata = soup.find('div', {'class': '_FOc'})
		predata1 = soup.find('div', {'class': 'vk_gy _KNe vk_h'})
		predata2 = predata.find('span', {'class': '_Rnb fmob_pr fac-l'})
		data = predata.text.strip()
		data1 = predata1.text.strip()
		data3 = predata2.text.strip()
		ofile.write(data1+" "+data + '\n')
		ofile.close()
		print(data3)
		#with open(file2, 'a') as ingraph:
			#ingraph.writelines(data3+'\n')
			#ingraph.close()
		
		
#stocks1(Stock1)
#stocks1(Stock2)
#stocks1(Stock3)
"""
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
		ofile.write(data+" "+data1)
		ofile.close()
						
stocks2(Stock2)
"""

