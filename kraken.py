import krakenex, os

key = os.environ['KRAKEN_KEY']
k = krakenex.API()
k.load_key('kraken.key')

print k.query_private('Balance')

print k.query_public('Ticker', {'pair': 'XXBTZUSD'})
