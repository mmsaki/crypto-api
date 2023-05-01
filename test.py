import requests
import json

# Block number
blocknumber = requests.get('http://127.0.0.1:5000/latestBlock').json()
print(f'Response : {blocknumber}')

# Balance of account
address = '0x04655832bcb0a9a0bE8c5AB71E4D311464c97AF5'
balance = requests.get(f'http://127.0.0.1:5000/getBalance/{address}').json()
print(f'Response : {balance}')

# Transaction hash
hash = '0x5add506dfbcb2a390545a5c4975d82790ab2d0622582997b02710ac74473fcad'
tx_data = requests.get(f'http://127.0.0.1:5000/tx/{hash}').json()
print(f'Response : {tx_data}')
