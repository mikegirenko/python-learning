import re
import requests
from bs4 import BeautifulSoup
"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.

"""

# Make API call to get data from the website
URL = "http://www.nytimes.com/"
r = requests.get(URL)
r_html = r.content

# Parse response
soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.find_all({'h2': re.compile('esl82me0')})

# Split each record and print title only
for title in titles:
    first_split = str(title).split('>')
    second_split = str(first_split[1]).split('<')
    print(second_split[0])
