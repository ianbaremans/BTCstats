# importing the necessary modules
from lxml import html
import requests 
import asciimatics

# getting the webpage with data and parse it to tree
page = requests.get("http://blockchained.com/")
tree = html.fromstring(page.content)

# store data from webpage in vars
btc_price_usd = tree.xpath("//*[@id='container']/font[1]/b/text()")
btc_price_eur = tree.xpath("//*[@id='container']/font[2]/b/text()")

print(btc_price_usd)
print(btc_price_eur)
