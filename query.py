import json
import requests


def query_balance(url, username, password):
	session = requests.Session()
	session.auth = requests.auth.HTTPDigestAuth(username, password)
	data = {"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0}}
	headers = {'Content-Type': 'application/json'}
	print(session.get(url, data=json.dumps(data), headers=headers).json())

if __name__ == '__main__':
	url = "https://xmr.com/json_rpc"
	username = "shallwe"
	password = "shallwe's mima"
	query_balance(url, username, password)