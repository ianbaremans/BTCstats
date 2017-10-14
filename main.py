# importing the necessary modules
from lxml import html
import requests 
import re
from time import sleep
import curses

# ascii art title
title = "  ____ _____ _______ _____ ____ _____ _   _ ".center(63)+"\n"
title += " |  _ \_   _|__   __/ ____/ __ \_   _| \ | |".center(63)+"\n"
title += " | |_) || |    | | | |   | |  | || | |  \| |".center(63)+"\n"
title += " |  _ < | |    | | | |   | |  | || | | . ` |".center(63)+"\n"
title += " | |_) || |_   | | | |___| |__| || |_| |\  |".center(63)+"\n"
title += " |____/_____|  |_|  \_____\____/_____|_| \_|".center(63)+"\n"

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
btc_price_usd = btc_price_usd[2:-2].center(11)
btc_price_eur = btc_price_eur[2:-2].center(11)
btc_market_cap = btc_market_cap[:-9].center(23)
btc_generated = btc_generated[:-5].center(13)

data = " "+"="*63+"\n"
data += " |    USD    |    EUR    |   MARKET CAP in USD   |    COINS    |\n "
data += "="*63+"\n"
data += " |{}|{}|{}|{}|\n ".format(
    btc_price_usd, btc_price_eur, btc_market_cap, btc_generated)
data += "="*63+"\n"
window = curses.initscr()
window.clear()
window.addstr(title)
window.addstr(data)
window.refresh()
window.getkey()

