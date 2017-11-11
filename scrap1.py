from bs4 import BeautifulSoup
import urllib.request


url = ("https://www.coindesk.com")
content = urllib.request.Request(url, data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })

z = urllib.request.urlopen(content).read()
soup = BeautifulSoup(z, "html.parser")
#data = soup.find('h4', attrs = {'class': 'heading'})

#plain_text = data.text.strip()
#print(plain_text)
print(soup)

