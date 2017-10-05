# importing the necessary modules
from lxml import html
import requests 
import asciimatics

# getting the webpage with data and parse it to tree
page = requests.get("https://charts.bitcoin.com/")
tree = html.fromstring(page.content)
