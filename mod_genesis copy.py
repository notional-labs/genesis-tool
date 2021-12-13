from numpy import add
import dig_sale 
import blurt_airdrop
import pandas as pd
import sys
import json
import copy

path_genesis = "/Users/khanh/dig/networks/mainnet/genesis.json"
path_excel = "/Users/khanh/Documents/lansauchithemvaofilenay2.xlsx"

old_genesis = "/Users/khanh/dig/networks/mainnet/testnet-4/genesis.json"

accounts_map = dig_sale.ReadExcelFile(path_excel)

def GetAccountListFromGenesis(genesis):
    acc_list = {}
    for id, bank_balance in enumerate(genesis['app_state']['bank']['balances']):
        acc_list[bank_balance['address']] = id
    return acc_list

f = open(path_genesis, "r")

genesis = json.load(f)

default_vesting_acc = {
    "@type" : "/cosmos.vesting.v1beta1.ContinuousVestingAccount",
    "base_vesting_account" : {
        "base_account": {
            "address": "",
            "pub_key": None,
            "account_number": "0",
            "sequence": "0"
        },
        "original_vesting": [
            {
            "denom": "udig",
            "amount": ""
            }
        ],
        "delegated_free": [],
        "delegated_vesting": [],
        "end_time": ""
    },
    "start_time": ""
}

default_auth_acc = {
    "@type": "/cosmos.auth.v1beta1.BaseAccount",
    "address": "",
    "pub_key": None,
    "account_number": "0",
    "sequence": "0"
}

default_bank_acc = {
    "address": "",
    "coins": [
    {
        "denom": "udig",
        "amount": "0"
    }
    ]
}

auth_accs = genesis['app_state']['auth']['accounts']

bank_accs = genesis['app_state']['bank']['balances']

acc_list = GetAccountListFromGenesis(genesis)

for bank_acc in bank_accs:
    bank_acc["coins"][0]["amount"] = str(bank_acc["coins"][0]["amount"])

for auth_acc in auth_accs:
    auth_acc["sequence"] = str(auth_acc["sequence"])
    auth_acc["account_number"] = str(auth_acc["account_number"])


sum_n = 0
for account, balance in accounts_map.items():

    if acc_list.get(account) != None:
        acc_id = acc_list[account]
        if balance < 0:
            balance = 1            
        bank_accs[acc_id]["coins"][0]["amount"] = str(balance)
        print("modify acc: " + account + " " + str(balance))
        sum_n += balance
    else :
        if balance < 0:
            balance = 1
        auth_acc = copy.deepcopy(default_auth_acc)
        auth_acc['address'] = account
        auth_accs.append(auth_acc)

        bank_acc = copy.deepcopy(default_bank_acc)
        bank_acc['address'] = account
        bank_acc["coins"][0]["amount"] = str(balance)
        bank_accs.append(bank_acc)
        sum_n += balance
        print("add new acc: " + account + " " + str(balance))
    
print(sum_n)
f = open(path_genesis, "w")
json.dump(genesis, f, indent=2)


