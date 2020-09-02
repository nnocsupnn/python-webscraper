from src.Binance import Binance
from src.Blockchain import Blockchain
from src.Bitmex import Bitmex

import time
import os
from sys import exit, argv, exc_info

validArgs = ['binance', 'blockchain', 'bitmex']

try:
    if len(argv) <= 1:
        raise Exception('Please define source.')
    else:
        if argv[1] not in validArgs:
            raise Exception('Source is not valid. [binance, blockchain]')

        PATH = "src/bin/chromedriver"
        if os.name == 'nt':
            PATH = "src/bin/chromedriver.exe"

        print("Starting getting", argv[1], "btc value.")

        # Defining per class is the easiest way to implement expantion of the scraping class.
        if argv[1] == 'binance':
            # Binance - Pattern
            binance = Binance("https://www.binance.com/en/trade/BTC_USDT")
            binance.scrape(PATH)

        elif argv[1] == 'blockchain':
            # Blockchain - Pattern
            blockChain = Blockchain("https://exchange.blockchain.com/trade")
            blockChain.scrape(PATH)

        elif argv[1] == 'blockchain':
            # Blockchain - Pattern
            blockChain = Blockchain("https://exchange.blockchain.com/trade")
            blockChain.scrape(PATH)

        elif argv[1] == 'bitmex':
            # Blockchain - Pattern
            blockChain = Bitmex("https://www.bitmex.com/app/trade/XBTUSD")
            blockChain.scrape(PATH)

except Exception as error:
    print("Oops! Error Caught:", error)
    exit(0)
