import sys, os
from iota import Iota
from iota import Address

# Read out seed to use from file
with open(os.path.join(sys.path[0], "seed_testnet"), "r") as f:
    seed = f.read()

# Connect to node using this seed
api = Iota("https://nodes.devnet.iota.org:443", seed, testnet = True)

# Ask user for number of addresses
count = int(input("How many addresses do you want to generate?"))

# Generate new address and print them
response = api.get_new_addresses(index=0, count=count, security_level=1)
for address in response["addresses"]:
    print(address)
