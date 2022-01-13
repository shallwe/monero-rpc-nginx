# monero-rpc-nginx
How to configure monero-rpc 

## Setup wallet-rpc.service
monero wallet can run client rpc by  `monero-wallet-rpc`, and listen to a port, like 10000, then you can use http to operate wallet and xmr coin with `http://localhost:10000/json_rpc`, doc in [doc][json_rpc] .

For security, you need to config login password, you should specify password in rpc-login and in monero-rpc.conf 

## Setup nginx and config proxy
And for security, you'd better call the rpc via https, while the nginx conf of monero-rpc is a bit strange.
In the conf.d/xmr.conf , proxy setting is strange.

```
upstream monerowallet {
  server 127.0.0.1:10019;
  keepalive 64;
 }
 location / {
  proxy_set_header Connection "";
  proxy_pass http://monerowallet;
  proxy_http_version 1.1;
  proxy_read_timeout 600s;
}
```

## Call the rpc via python
Remember to change the url, and specify the password

```
import json
import requests
session = requests.Session()
session.auth = requests.auth.HTTPDigestAuth('shallwe', 'shallwe.pass')
url = "https://xmr.shallwe.net/json_rpc"
data = {"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0}}
headers = {'Content-Type': 'application/json'}
session.get(url, data=json.dumps(data), headers=headers).json()
```

now you can get 
```
{..., 'jsonrpc': '2.0', 'result': {'balance': 0, ...
```


[json_rpc]: https://www.getmonero.org/resources/developer-guides/wallet-rpc.html