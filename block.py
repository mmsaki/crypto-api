from datetime import datetime
import web3_helper
from flask import jsonify


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def get_latest():
    return jsonify({"blockNumber": web3_helper.latestBlock()})
