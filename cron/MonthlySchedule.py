# -*- coding: utf-8 -*-
# __author__ = 'TOANTV'
import json
from bcolors import bcolors
from network_connector import NetworkConnection

# Init object
server_addr = "127.0.0.1"
server_port = "8000"
client = NetworkConnection(server_addr, server_port)

# Login
login_data = {"email": "le27l@mtholyoke.edu", "password": "linhlinh"}
headers = {'content-type': 'application/json'}
response = client.connect("POST", "/api/login/", data=json.dumps(login_data), headers=headers)
if response.status_code == 200:
    if hasattr(response, 'json') and isinstance(response.json(), dict):
        data = response.json()
        if "token" in data:
            headers["one-token"] = response.json()
else:
    bcolors.error("Cannot login to server!!!")


# Generate Monthly Schedule
client.connect("POST", "/api/working/generate/", headers=headers)