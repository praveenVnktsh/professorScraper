from bs4 import BeautifulSoup
import requests
import re

html_page = requests.get('https://www.ee.ucla.edu/all-faculty/')
soup = BeautifulSoup(html_page.text)
links = []
with open('ucla.csv', 'w') as f:
    for link in soup.findAll('div'):
        classs = link.get('class')
        style = link.get('style')
        if classs is not None and style is not None:
            if 'wp-block-column' in classs and 'flex-basis:66.66%' in style:
                # links.append(link.text)
                # print(link.text)
                stuff = link.text.split('\n')
                name = stuff[1].strip().replace(',',';')
                interests = stuff[2].strip().replace(',',';')
                f.write(f'{name},{interests}\n')
                


