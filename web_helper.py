from web3 import Web3

node = 'https://mainnet.infura.io/v3/6f57c3aef2854bd482f67669efec3acd'
web3 = Web3(Web3.HTTPProvider(node))


def blocknumber():
    return web3.eth.block_number


def getBlock():
    return web3.eth.get_block(blocknumber())


def getBalance(address):
    checked_address = Web3.to_checksum_address(address)
    return web3.eth.get_balance(checked_address) / 10 ** 18


def getTansaction(tx):
    return web3.eth.get_transaction(tx)
