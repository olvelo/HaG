import sys, os
from iota import Iota
from iota import Address

# Connect to node
api = Iota("https://nodes.devnet.iota.org:443", testnet = True)

# Read out address to use from file
address = []
with open(os.path.join(sys.path[0], "addresses_testnet"), "r") as f:
    address.append(f.read())

def getbalance():
    print("Checking balance")
    return api.get_balances(address)["balances"]
    
balance = getbalance()
print(balance)