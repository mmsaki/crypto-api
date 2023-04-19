from flask import Flask, request, jsonify
import web_helper


app = Flask(__name__)


@app.route("/")
def index():
    return "River API"


@app.route("/blocknumber")
def block_number():
    return jsonify({"blocknumber": web_helper.blocknumber()})


@app.route('/getBalance/<address>')
def getBalance(address):
    balance = web_helper.getBalance(address)
    return jsonify({"balance": balance})


@app.route('/tx/<hash>')
def getTransaction(hash):
    data = web_helper.getTansaction(hash)
    tx_dict = dict(data)

    # convert bytes instances to hexidecimal string representations
    for k, v in tx_dict.items():
        if isinstance(v, bytes):
            tx_dict[k] = v.hex()

    return jsonify({"tx": tx_dict})


if __name__ == "__main__":
    app.run(debug=True)
