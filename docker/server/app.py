from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)


# make a new account
# createwallet
# takes in 
# name: (either the project id, for project accounts or the user id for user accounts)
@app.route("/api/createwallet", methods=['POST', 'GET'])
def createwallet():
    if request.method == 'POST':
      url = 'http://derek:iamapassword123@172.33.0.6:9776'
      name = [request.form['name']]

      payload = {
        "method": "createwallet",
        "params": name,
        "jsonrpc": "2.0",
        "id": 0
      }
      response = requests.post(url, json=payload).json()

      if response['error']:
        return jsonify(response)
      else:
        url = 'http://derek:iamapassword123@172.33.0.6:9776/wallet/{}'.format(response['result']['name'])
        print(url)
        payload = {
          "method": "getnewaddress",
          "jsonrpc": "2.0",
          "id": 0
        }
        address_response = requests.post(url, json=payload).json()
        address_response['name'] = response['result']['name']
        address_response['warning'] = response['result']['warning']

      return jsonify(address_response)
    else:
      return "Incorrect method"

# for backing projects
# sendtoaddress
# takes in 
# from: name of the wallet sending
# to: address of the wallet receiving
# amount: amount of coin being sent
@app.route("/api/sendtoaddress", methods=['POST', 'GET'])
def move():
    if request.method == 'POST':
      url = 'http://derek:iamapassword123@172.33.0.6:9776/wallet/{}'.format(request.form['from'])
      sent_to = request.form['to']
      amount = float(request.form['amount'])
      params = [sent_to, amount]

      payload = {
        "method": "sendtoaddress",
        "params": params,
        "jsonrpc": "2.0",
        "id": 0
      }

      response = requests.post(url, json=payload).json()
      print(response)
      return jsonify(response)
    else:
      return "Incorrect method"

# for telling users their balance and for checking the balance of projects
# get balance
# takes in 
# wallet: name of the wallet who's balance is being gotten
@app.route("/api/getbalance", methods=['POST', 'GET'])
def getbalance():
    if request.method == 'POST':
      url = 'http://derek:iamapassword123@172.33.0.6:9776/wallet/{}'.format(request.form['wallet'])

      payload = {
        "method": "getbalance",
        "jsonrpc": "2.0",
        "id": 0
      }

      response = requests.post(url, json=payload).json()
      return jsonify(response)
    else:
      return "Incorrect method"
