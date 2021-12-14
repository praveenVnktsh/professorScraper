from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm 

html_page = requests.get('https://www.ece.utexas.edu/people/faculty')
soup = BeautifulSoup(html_page.text)
links = []
with open('utAustin.csv', 'w') as f:
    for link in tqdm(soup.find_all('div')):

        classs = link.get('class')
        if classs is not None and 'views-field-title' in classs:

            url = link.findNextSiblings()
            for l in url:
                url = l.find('a', href = True)
                if url is not None:
                    url = url.get('href')
                    if '/people/faculty/' in url:
                        
                        break
            print(url)
            if url is None:
                continue
            html_page2 = requests.get(f"https://www.ece.utexas.edu{url}")
            soup2 = BeautifulSoup(html_page2.text) 

            area = None
            interests = None
                
            for div in soup2.find_all('div'):
                classs = div.get('class')
                if classs is not None:
                    if 'field--name-field-research-areas' in classs:
                            area = div.text
                            print(area)
                            area = area.strip().replace('Research Areas','').replace(',',';').replace('&amp;','&').replace('\n',';')

                    if 'field--name-field-research-interests' in classs:
                            interests = div.text
                            print(interests)
                            interests = interests.strip().replace('Research Interests','').replace(',',';').replace('&amp;','&').replace('\n',';')
            f.write(f"https://www.ece.utexas.edu{url},{area},{interests}\n")
