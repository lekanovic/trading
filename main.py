import cexapi, os

username = os.environ['CEX_USER']
key = os.environ['CEX_KEY']
secret = os.environ['CEX_SECRET']

demo = cexapi.API(username, key, secret)

print demo.ticker()
print demo.balance()
