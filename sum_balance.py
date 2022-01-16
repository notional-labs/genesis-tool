import genesis_util
import json

f = open("/Users/khanh/dig/networks/mainnets/dig-1/genesis.json", "r")
genesis = json.load(f)

bank_balances = genesis_util.GetBankBalancesFromGenesis(genesis)
g = open("dfy", "w")
sum = 0
for bank_balance in bank_balances:
    amount = genesis_util.GetAmountFromBankBalance(bank_balance)
    sum += amount
    if bank_balance['address'][:2] == "0x": 
        g.writelines(bank_balance["address"] + "," + bank_balance['coins'][0]["amount"] + "\n")
g.close()


print(sum)