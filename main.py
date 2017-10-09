# importing the necessary modules
from lxml import html
import requests 
import asciimatics
import re

# getting the webpage with data and parse it to tree
page = requests.get("http://blockchained.com/")
tree = html.fromstring(page.content)
page.text

# regex for btc generated and market cap
match_generated = re.search(r"(Coins\ generated\: )(.*)", page.text)
match_market_cap = re.search(r"(Market\ cap\: )(.*)", page.text)

# store data from webpage in vars
btc_price_usd = tree.xpath("//*[@id='container']/font[1]/b/text()")
btc_price_eur = tree.xpath("//*[@id='container']/font[2]/b/text()")
btc_generated = match_generated.group(2)
btc_market_cap = match_market_cap.group(2)

# slicing the strings to remove html tags
btc_market_cap = btc_market_cap[:-5]
btc_generated = btc_generated[:-5]

# printing the data for testing
print(btc_price_usd)
print(btc_price_eur)
print(btc_generated)
print(btc_market_cap)

