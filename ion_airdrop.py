import bech32

import csv

fDir = "ion_airdrop.csv"

total = 30000000000000





# for k, v in mydict.items() :
#     print(k)
#     hex = bech32.decode('cosmos', k)
#     print(hex)
#     dig = bech32.encode('dig', version, hex)
#     print(dig)
#     break 

import json
import sys


def read_export_and_write_balances_to_file():
    dirIn = sys.argv[1]
    dirOut = sys.argv[2]
    print(dirIn, dirOut)
    f = open(dirIn, 'r')
    g = open(dirOut, 'w')
    state_export = json.load(f)
    account_balances = state_export["app_state"]["bank"]["balances"]
    for account_balance in account_balances:
        print(account_balance)
        addr = account_balance["address"]
        coins = account_balance["coins"]
        if len(coins) != 0:
            if coins[0]["denom"] == "uion":
                amount = coins[0]["amount"]
                g.writelines(addr + "," + amount + '\n')
    f.close()
    g.close()

def get_ions():
    with open(fDir, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
    total_ion = 0
    for addr, balance in mydict.items():
        total_ion += int(balance)
    m = {}
    sum = 0
    for addr, balance in mydict.items() :
        addr = addr.strip().lower()
        _, addrBz = bech32.bech32_decode(addr)
        addr = bech32.bech32_encode('dig',addrBz)

        i = int(total * int(balance) / total_ion)
        
        m[addr] = i
        sum += i
    print("total ion airdrop:", sum)
    return m

get_ions()
# print(get_ions())        
        
