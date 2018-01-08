from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import re
import os
file = ("C:\Scratch\Python Scripts\Copy1.txt")
file1 = ("C:\Scratch\Python Scripts\copy2.txt")
file2 = ("C:\Scratch\Python Scripts\graph.txt")

#file's for the un-used sort function
file3 = ("C:\Scratch\Python Scripts\projstocks\in1.txt")
file4 = ("C:\Scratch\Python Scripts\projstocks\in2.txt")
file5 = ("C:\Scratch\Python Scripts\projstocks\in3.txt")

def trip(z):
	if z == len(c):
		return False
	else:
		return True
		
def search():
	Usersearch = input("What Australian stock would you like to monitor? (Exchange name) :")
	url = (f"https://www.google.com.au/search?dcr=0&ei=EnMvWuq1LoL-8QXFibDACQ&q=asx%3A{Usersearch}&oq=asx%3Atcc&gs_l=psy-ab.3..0i71k1l4.0.0.0.13118.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.TupNfg8lvIg")
	return url
"""
def sort(r):
	with open(file3, 'a') as in1:
		in1.write(r)
	with open(file4, 'a') as in2:
		in2.write(r)
	with open(file5, 'a') as in3:
		in3.write(r)


# Assigns the google search link to a variable which is used to pass to the function, need to make if statement????
with open(file1, 'r') as infile:
	data = infile.readlines()
	i = len(data)
	z = i - len(data)		
	Stock1 = data[0]
	Stock2 = data[1]
	Stock3 = data[2]
	#Stock4 = data[3]
		
		
	infile.close()
"""
	
#Can search for the stockname by user input, and extrat the first value of the stock per each line, using this to create a graph, truncating after
def graph():
	name = input("Which of your monitored stocks would you like to generate a graph for?")
	with open(file, 'r') as ingraph:
		data = ingraph.readlines()
		for line in data:
			if name in line:
				search = re.findall("\d+\.\d+", line)
				with open(file2, 'a') as outgraph:
					outgraph.write(search[0]+"\n")
													
	with open(file2, 'r+') as outgraph:
		data = outgraph.readlines()
		plt.plot(data)
		plt.show()
		outgraph.truncate(0)
	
#Takes the google stock link (S1) and extracts the data
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
		c.append(1)
		

		
c = []
count = int(input("How many days would you like to monitor the selected stocks for? "))
while len(c) < count:
	stocks1(search())
else:
	graph()
