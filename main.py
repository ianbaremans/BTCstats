# importing the necessary modules
from lxml import html
import requests 
import re
from time import sleep
import curses
from twisted.internet import task, reactor

# global vars
centervar = 63

# simple hack for resizing the gnome terminal window
print("\x1b[8;13;65t")
window = curses.initscr()

# ascii art title
title = "  ____ _____ _______ _____ ____ _____ _   _ ".center(centervar)+"\n"
title += " |  _ \_   _|__   __/ ____/ __ \_   _| \ | |".center(centervar)+"\n"
title += " | |_) || |    | | | |   | |  | || | |  \| |".center(centervar)+"\n"
title += " |  _ < | |    | | | |   | |  | || | | . ` |".center(centervar)+"\n"
title += " | |_) || |_   | | | |___| |__| || |_| |\  |".center(centervar)+"\n"
title += " |____/_____|  |_|  \_____\____/_____|_| \_|".center(centervar)+"\n"

def build_cli():
    # getting the webpage with data and parse it to tree
    page = requests.get("http://blockchained.com/")
    tree = html.fromstring(page.content)
    match_page = page.text.replace("&nbsp;", " ")

    # regex for btc generated, market cap and bitstamp
    match_generated = re.search(r"(Coins\ generated\: )(.*)", match_page)
    match_market_cap = re.search(r"(Market\ cap\: )(.*)", match_page)
    match_bitstamp = re.search(r"(Bitstamp\ (.*)\ min\.\ ago)", match_page) 

    # store data from webpage in vars
    btc_price_usd = tree.xpath("//*[@id='container']/font[1]/b/text()")
    btc_price_eur = tree.xpath("//*[@id='container']/font[2]/b/text()")
    btc_generated = match_generated.group(2)
    btc_market_cap = match_market_cap.group(2)
    bitstamp = match_bitstamp.group(1)

    # slicing the strings to remove unnecessary tags and centering in the cli
    btc_price_usd = str(btc_price_usd)
    btc_price_eur = str(btc_price_eur)
    btc_price_usd = btc_price_usd[2:-2].center(11)
    btc_price_eur = btc_price_eur[2:-2].center(11)
    btc_market_cap = btc_market_cap[:-9].center(23)
    btc_generated = btc_generated[:-5].center(13)
    bitstamp = bitstamp.center(centervar)

    # building the table for the cli
    data = " "+"="*centervar+"\n"
    data += " |    USD    |    EUR    |   MARKET CAP in USD   |    COINS    |\n "
    data += "="*centervar+"\n"
    data += " |{}|{}|{}|{}|\n ".format(
        btc_price_usd, btc_price_eur, btc_market_cap, btc_generated)
    data += "="*centervar+"\n"

    # building the cli
    window.clear()
    window.addstr(title)
    window.addstr(data)
    window.addstr(bitstamp)
    window.refresh()
    
while 1:
    build_cli()
    sleep(1)

