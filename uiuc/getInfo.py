from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm 

html_page = requests.get('https://ece.illinois.edu/about/directory/faculty')
soup = BeautifulSoup(html_page.text)
links = []
with open('uiuc.csv', 'w') as f:
    for link in tqdm(soup.find_all('a', href=True)):
        if "/about/directory/faculty/" in link['href']:
            html_page2 = requests.get("https://ece.illinois.edu/"+link['href'])
            soup2 = BeautifulSoup(html_page2.text) 

            temp = []
            # find all ui under the h2 tag of research interests in the soup2
            for h2 in soup2.find_all('h2'):

                if h2.text == "Research Interests" or h2.text == "Research Topics":

                    for sub in h2.findNextSiblings():
                        if sub.name == 'ul':
                            temp.extend(sub.text.strip().split('\n'))

                        else:
                            if sub.name == 'h2':
                                break
            
            if len(temp) > 0:
                f.write(f"{'https://ece.illinois.edu/'+link['href']},{','.join(temp)}\n")
