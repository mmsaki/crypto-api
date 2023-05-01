import os
from dotenv import load_dotenv
from web3.middleware.cache import construct_simple_cache_middleware
from flask import Flask, request, jsonify, render_template
import connexion
import web3_helper
import utils
from web3 import Web3

app = connexion.App(__name__, specification_dir='./')
app.add_api("swagger.yml")


@app.route("/")
def index():
    return render_template("home.html")


# @app.route("/latestBlock")
# def block_number():
#     return jsonify({"Latest Block": web3_helper.latestBlock()})


# @app.route("/getBlock/<number>")
# def getBlock(number):
#     block_data = web3_helper.getBlock(number)
#     parsed_hex = utils.JsonParseBlockData(block_data)
#     return jsonify({"data": parsed_hex})


# @app.route('/getBalance/<address>')
# def getBalance(address):
#     balance = web3_helper.getBalance(address)
#     return jsonify({"balance": balance})


# @app.route('/tx/<hash>')
# def getTransaction(hash):
#     data = web3_helper.getTansaction(hash)
#     hex_json = utils.JsonParserTransactionData(data)

#     return jsonify({"tx": hex_json})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
