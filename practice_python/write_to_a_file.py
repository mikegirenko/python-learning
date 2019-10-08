import re
import requests
from bs4 import BeautifulSoup

"""
Take the code from the How To Decode A Website exercise (if you didn’t do it 
or just want to play with some different code, use the code from the 
solution), and instead of printing the results to a screen, write the 
results to a txt file. In your code, just make up a name for the file 
you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved.
"""

URL = "http://www.nytimes.com/"
r = requests.get(URL)
text = r.text


soup = BeautifulSoup(text, 'html.parser')
titles = soup.find_all({'h2': re.compile('esl82me0')})

file_name = input("Enter filename: ")
with open(file_name, 'w') as file_object:
    file_object.write(str(titles))
    file_object.close()
