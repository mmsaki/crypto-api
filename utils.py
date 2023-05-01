from web3.utils import exception_handling
from hexbytes import HexBytes
from web3._utils.type_conversion import to_hex_if_bytes


def JsonParserTransactionData(data):
    tx_dict = dict(data)
    for k, v in tx_dict.items():
        if isinstance(v, bytes):
            tx_dict[k] = v.hex()

    return tx_dict


def JsonParseBlockData(data):
    tx_dict = dict(data)
    for key, val in tx_dict.items():
        if isinstance(val, HexBytes):
            tx_dict[key] = to_hex_if_bytes(val)
        if key == "transactions":
            for i, v in enumerate(val):
                tx_dict[key][i] = to_hex_if_bytes(bytes(v))
        if key == "withdrawals":
            for i, v in enumerate(val):
                tx_dict[key][i] = dict(v)  # type: ignore
    return tx_dict
