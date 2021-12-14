from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm

with open('purdueLinks.txt', 'r') as f:
    links = f.readlines()

with open('purdueResearch1.csv', 'w') as f:
    for link in tqdm(links):
        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.text, features = 'lxml')
        for link in soup.findAll('title'):
            name = link.text.split('-')[0].strip().replace('\n', ' ')

        for link in soup.findAll('p'):
            ls = link.get('class')
            if ls is not None:
                if 'profile-research' in ls:
                    researchInterests = link.text.strip().replace('\n', ' ')
        for link in soup.findAll('div'):
            ls = link.get('class')
            if ls is not None:
                if 'profile-titles' in ls:
                    title = link.text.strip().replace('\n', ' ')

        f.write(f'{name}&&{title}&&{researchInterests}&&{link}\n')
        
