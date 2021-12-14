from bs4 import BeautifulSoup
import requests
import re

html_page = requests.get('https://engineering.purdue.edu/ECE/Faculty')
soup = BeautifulSoup(html_page.text)
links = []
with open('purdue.txt', 'w') as f:
    for link in soup.findAll('a'):
        l = link.get('href')
        if 'https://engineering.purdue.edu/ECE/People/ptProfile?resource_id=' in l:
            links.append(l)


