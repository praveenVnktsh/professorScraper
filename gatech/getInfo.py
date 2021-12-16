from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm 

html_page = requests.get('https://www.ece.gatech.edu/faculty-staff-directory?')
soup = BeautifulSoup(html_page.text)
links = []
with open('gatech.csv', 'w') as f:
    links = soup.find_all('a', href=True)
    for i,link in enumerate(tqdm(links)):
        if "/faculty-staff-directory/" in link['href']:
            next_link = links[i+1]
            if "mailto" in next_link["href"]:
                html_page2 = requests.get("https://www.ece.gatech.edu"+link['href'])
                soup2 = BeautifulSoup(html_page2.text) 

                temp = []
                # find all ui under the h2 tag of research interests in the soup2
                for div in soup2.find_all('div'):
                    classs = div.get('class')

                    if classs is not None:    
                        
                        if "Research interests:" in div.text:
                            if "field-name-field-research-interests" in classs:
                                temp.extend(div.text.strip().split("\n")[1:]) 
                
                if len(temp) > 0:
                    f.write(f"{'https://ece.illinois.edu/'+link['href']},{','.join(temp)}\n")
