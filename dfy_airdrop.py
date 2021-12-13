import genesis_util
import json


def get_dfy_airdrop():
    f = open("genesis.json", 'r')
    genesis = json.load(f)

    accs = {}
    bank_balances_from_old_genesis = genesis_util.GetBankBalancesFromGenesis(genesis)
    for bank_balance in bank_balances_from_old_genesis:
        addr = bank_balance["address"].strip().lower()
        if addr[:2] == "0x":
            accs[addr] = genesis_util.GetAmountFromBankBalance(bank_balance)
    return accs

