import sys, os
from iota import Iota
from iota import Address

# Connect to node
api = Iota("https://nodes.devnet.iota.org:443", testnet = True)

# Read out address to use from file
addresses = []
with open(os.path.join(sys.path[0], "addresses_testnet"), "r") as f:
    for line in f.readlines():
        addresses.append(line.strip())

print(addresses)

def getbalance():
    print("Checking balance")
    return api.get_balances(addresses)["balances"]
    
balance = getbalance()
print(balance)

spent = api.were_addresses_spent_from(addresses)
print(spent)
