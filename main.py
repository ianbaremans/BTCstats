# importing the necessary modules
from __future__ import division
from lxml import html
import requests 
import asciimatics
import re
from asciimatics.screen import Screen
from time import sleep
from asciimatics.effects import Print
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

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

# slicing the strings to remove unnecessary tags
btc_price_usd = str(btc_price_usd)
btc_price_eur = str(btc_price_eur)
btc_price_usd = btc_price_usd[2:-2]
btc_price_eur = btc_price_eur[2:-2]
btc_market_cap = btc_market_cap[:-5]
btc_generated = btc_generated[:-5]

def gui(screen):
    effects = [
        Print(screen,FigletText("BITCOIN", font="big"), screen.height // 3 - 8),
    ]
    screen.play([Scene(effects, 0)])

Screen.wrapper(gui)

