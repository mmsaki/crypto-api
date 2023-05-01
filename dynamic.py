from web3 import Web3
from dotenv import load_dotenv
import os
import web3_helper
from eth_account import Account
import utils

load_dotenv()
INFURA = os.getenv('INFURA_KEY')
endpoint = f"https://mainnet.infura.io/v3/{INFURA}"

w3 = Web3(Web3.HTTPProvider(endpoint))
acct = w3.eth.account.from_key(os.environ.get('PRIVATE_KEY'))

tx = acct

block = w3.eth.get_block(3322437)
print(utils.JsonParserTransactionData(block))
