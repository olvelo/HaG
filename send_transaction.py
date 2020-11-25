import sys, os
from iota import Iota, Address, ProposedTransaction

# Read out seed to use from file
with open(os.path.join(sys.path[0], "seed_testnet"), "r") as f:
    seed = f.read()

# Connect to node using this seed
api = Iota("https://nodes.devnet.iota.org:443", seed, testnet = True)

# Read out address to use from file
addresses = []
with open(os.path.join(sys.path[0], "addresses_testnet"), "r") as f:
    for line in f.readlines():
        addresses.append(line.strip())

tx = ProposedTransaction(address=Address(addresses[1]), value=1)
print("Sending 1 iota to " + addresses[1])

result = api.send_transfer(transfers=[tx])
print(result["bundle"].hash)