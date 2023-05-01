from web3 import Web3
from web3.middleware.cache import construct_simple_cache_middleware
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("INFURA_KEY")

node = 'https://sepolia.infura.io/v3/' + str(api_key)
web3 = Web3(Web3.HTTPProvider(node))

web3.middleware_onion.add(construct_simple_cache_middleware())


def latestBlock():
    print(web3.eth.__doc__)
    return web3.eth.block_number


def getBlock(number):
    return web3.eth.get_block(number)


def getBalance(address):
    checked_address = Web3.to_checksum_address(address)
    return web3.eth.get_balance(checked_address) / 10 ** 18


def getTansaction(tx):
    return web3.eth.get_transaction(tx)
