from iota import Iota
from iota import Address

iotaNode = "https://node1.rosipay.net:443"

"""
api = Iota(iotaNode, "")
address = [Address(b'NYZBHOVSMDWWABXSACAJTTWJOQRPVVAWLBSFQVSJSWWBJJLLSQKNZFC9XCRPQSVFQZPBJCJRANNPVMMEZQJRQSVVGZ')]
gb_result = api.get_balances(address)
balance = gb_result['balances']
print("Balance of some random address: " + str(balance[0]))
"""

seed = 'RWCX9QOBHEKGIYZHIZOVSIRHKFF9QVPEIQBSQKHXMFODEQHEWPWCHDZAXHJJNQWIJINYVJZVTGBHSDY9S'
api = Iota("https://node1.rosipay.net:443", seed, testnet = True)
address = api.get_new_addresses(index=0, count=1, security_level=2)['addresses'][0]
is_spent = api.were_addresses_spent_from([address])['states'][0]
print(address)
print(is_spent)
