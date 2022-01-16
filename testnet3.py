import genesis_util
import json

dir = "/Users/khanh/dig/networks/testnets/testnet-3/genesis.json"

def get_substracting_accs():
    nukes = {}
    f = open(dir, 'r')
    genesis = json.load(f)
    bank_balances = genesis_util.GetBankBalancesFromGenesis(genesis)
    for bank_balance in bank_balances:
        addr = bank_balance["address"]
        if addr[:4] == "dig1" :
            nukes[addr] = genesis_util.GetAmountFromBankBalance(bank_balance)
    return nukes

