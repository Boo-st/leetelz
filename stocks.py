from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import re
import datetime
file = ("/Users/mitchelking/Documents/Stocklinks/Stocklinks.txt")
file1 = ("/Users/mitchelking/Documents/Stocks/Stocks.txt")
file2 = ("/Users/mitchelking/Documents/Stocks/Graph.txt")

# For function sort and then to count howmany links in the file and create a variagle for each
#file3 = ("C:\Scratch\Python Scripts\projstocks\in1.txt")
#file4 = ("C:\Scratch\Python Scripts\projstocks\in2.txt")  
#file5 = ("C:\Scratch\Python Scripts\projstocks\in3.txt")


class stocks:


	now = str(datetime.date.today())
	count = int(input("How many days would you like to monitor the selected stocks for? "))


	def trip():
		now = str(datetime.date.today())
		trigger = now[8] + now[9]
		return count + int(trigger)

	def search():	
		Usersearch = input("What Australian stock would you like to monitor? (Exchange name) :")
		url = (f"https://www.google.com.au/search?dcr=0&ei=EnMvWuq1LoL-8QXFibDACQ&q=asx%3A{Usersearch}&oq=asx%3Atcc&gs_l=psy-ab.3..0i71k1l4.0.0.0.13118.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.TupNfg8lvIg")
		return url

#Can search for the stockname by user input, and extrat the first value of the stock in the data file, using this to create a graph
	def graph(z):
		#Keyword = input("What stock would you like to generate a graph for? ")
		with open(file, 'r') as ingraph:
			data = ingraph.readlines()
			for line in data:
				if (z) in line:
					search = re.findall("\d+\.\d+", line)
					with open(file2, 'a') as outgraph:
						outgraph.write(search[0]+"\n")
						
						
		with open(file2, 'r') as outgraph:
			data = outgraph.readlines()
			plt.plot(data)
			plt.show()
			outgraph.truncate(0)
		
#graph()
	
	
#Takes the google stock link (S1) and extracts the data
	def stocks1(S1):
		# not trip(count):
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
				#ofile.write(data1+" "+data + '\n')
				ofile.close()
				c.append(1)
				print(data3)
				return True
		
	c = []		
		
	while stocks1(search()):
		stocks1(search())
		print(len(c))



