import json
import copy

# default_vesting_acc used to make new vesting acc for an addr to put into genesis.json auth
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
            "denom": "uan1",
            "amount": ""
            }
        ],
        "delegated_free": [],
        "delegated_vesting": [],
        "end_time": "1702603072"
    },
    "start_time": "1639531072"
}

# default_auth_acc used to make new auth acc for an addr to put into genesis.json auth
default_auth_base_acc = {
    "@type": "/cosmos.auth.v1beta1.BaseAccount",
    "address": "",
    "pub_key": None,
    "account_number": "0",
    "sequence": "0"
}

# default_bank_acc used to make new bank balance for an addr to put into genesis bank
default_bank_balance = {
    "address": "",
    "coins": [
        {
            "denom": "uan1",
            "amount": "0"
        }
    ]
}

def MapFromAddressToBankIdFromGenesis(genesis):
    map_addr_to_bank_balance_id = {}
    for id, bank_balance in enumerate(genesis['app_state']['bank']['balances']):
        map_addr_to_bank_balance_id[bank_balance['address'].lower()] = id
    return map_addr_to_bank_balance_id

def MapFromAddressToAuthIdFromGenesis(genesis):
    map_addr_to_auth_acc_id = {}
    for id, auth_balance in enumerate(genesis['app_state']['auth']['accounts']):
        try:
            map_addr_to_auth_acc_id[auth_balance['address'].lower()] = id
        except:
            map_addr_to_auth_acc_id[auth_balance['base_vesting_account']['base_account']['address'].lower()] = id
    return map_addr_to_auth_acc_id

def GetAuthAccsFromGenesis(genesis):
    return copy.deepcopy(genesis['app_state']['auth']['accounts'])

def GetBankBalancesFromGenesis(genesis):
    return copy.deepcopy(genesis['app_state']['bank']['balances'])

def SetAuthAccsForGenesis(genesis, auth_accs):
    genesis['app_state']['auth']['accounts'] = auth_accs

def SetBankBalancesForGenesis(genesis, bank_balances):
    genesis['app_state']['bank']['balances'] = bank_balances

def GetAmountFromBankBalance(bank_balance):
    return int(bank_balance['coins'][0]['amount'])

def SetAmountToBankBalance(bank_balance, amount):
    bank_balance['coins'][0]['amount'] = str(amount)

def CreateNewVestingAccount(addr, vesting_amount):
    vesting_auth_acc = copy.deepcopy(default_vesting_acc)
    vesting_auth_acc['base_vesting_account']['base_account']['address'] = addr
    vesting_auth_acc['base_vesting_account']['original_vesting'][0]['amount'] = str(vesting_amount)
    return vesting_auth_acc

def CreateNewAuthBaseAccount(addr):
    auth_acc = copy.deepcopy(default_auth_base_acc)
    auth_acc['address'] = addr
    return auth_acc

def AddNewAuthBaseAccount(auth_accs, addr):
    auth_acc = CreateNewAuthBaseAccount(addr)
    auth_accs.append(auth_acc)

def AddNewVestingAccount(auth_accs, addr, vesting_amount):
    vesting_auth_acc = CreateNewVestingAccount(addr, vesting_amount)
    auth_accs.append(vesting_auth_acc)

def CreateNewBankBalance(addr, amount):
    bank_balance = copy.deepcopy(default_bank_balance)
    bank_balance['address'] = addr
    bank_balance["coins"][0]["amount"] = str(amount)
    return bank_balance


# convert 
def ConvertAuthBaseAccountsToVestingAccounts(genesis_dir, converting_accs):
    g = open(genesis_dir, "r")
    genesis = json.load(g)

    auth_accs = GetAuthAccsFromGenesis(genesis)
    bank_balances = GetBankBalancesFromGenesis(genesis)
    map_addr_to_auth_acc_id = MapFromAddressToAuthIdFromGenesis(genesis)
    map_addr_to_bank_balances_id = MapFromAddressToBankIdFromGenesis(genesis)

    sum = 0
    for addr, vesting_amount in converting_accs.items():
        try:
            addr = addr.lower()

            auth_id = map_addr_to_auth_acc_id[addr]
            bank_id = map_addr_to_bank_balances_id[addr]

            print(auth_id, bank_id)

            bank_balance = bank_balances[bank_id]
            amount_in_bank = GetAmountFromBankBalance(bank_balance)

            if amount_in_bank < vesting_amount:
                print("error")
                continue

            vesting_auth_acc = CreateNewVestingAccount(addr, vesting_amount)

            auth_accs[auth_id] = vesting_auth_acc
            sum += vesting_amount
            print("vest acc with addr ", addr, " vesting_amount ", vesting_amount)
        except:
            pass
    SetAuthAccsForGenesis(genesis, auth_accs)

    print("total vested ammount:", sum)
    g.close()
    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)


# dump account map to genesis as auth base account with bank balance
def AddAccountsIntoGenesis(genesis_dir, accounts):

    g = open(genesis_dir, "r")
    genesis = json.load(g)

    map_addr_to_auth_id = MapFromAddressToAuthIdFromGenesis(genesis)

    bank_balances = GetBankBalancesFromGenesis(genesis)

    map_addr_to_bank_id = MapFromAddressToBankIdFromGenesis(genesis)

    auth_accs = GetAuthAccsFromGenesis(genesis)

    n = 0
    for addr, amount in accounts.items():
        if map_addr_to_auth_id.get(addr) != None:

            bank_id = map_addr_to_bank_id[addr]


            if amount < 0:
                bank_balances[bank_id] = 0
                auth_id = map_addr_to_auth_id[addr]

                auth_accs[auth_id] = 0
                continue


            # bank_balance = bank_balances[bank_id]
            # if GetAmountFromBankBalance(bank_balance) < 0:
            #     amount = 1            

            bank_balance = bank_balances[bank_id]
            SetAmountToBankBalance(bank_balance, GetAmountFromBankBalance(bank_balance) + amount)
            print("modify acc: " + addr + " " + str(amount))
            n += amount
        else :
            if amount < 0:
                amount = 1
                continue

            auth_acc = CreateNewAuthBaseAccount(addr)

            auth_accs.append(auth_acc)
            bank_balance = CreateNewBankBalance(addr, amount)

            bank_balances.append(bank_balance)
            n += amount
            print("add new acc: " + addr + " " + str(bank_balance))

    SetBankBalancesForGenesis(genesis, bank_balances)
    SetAuthAccsForGenesis(genesis, auth_accs)

    print("total added:", n)
    
    g.close()
    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)


# 
def AddVestingAccountsIntoGenesis(genesis_dir, accounts):
    g = open(genesis_dir, "r")
    genesis = json.load(g)

    map_addr_to_auth_id = MapFromAddressToAuthIdFromGenesis(genesis)

    bank_balances = GetBankBalancesFromGenesis(genesis)

    map_addr_to_bank_id = MapFromAddressToBankIdFromGenesis(genesis)

    auth_accs = GetAuthAccsFromGenesis(genesis)
    hmmm = ""
    n = 0
    for addr, vesting_amount in accounts.items():
        # already exist address in this
        if map_addr_to_auth_id.get(addr) != None:
            auth_id = map_addr_to_auth_id[addr]
            bank_id = map_addr_to_bank_id[addr]
            # bank_balance = bank_balances[bank_id]
            # if GetAmountFromBankBalance(bank_balance) < 0:
            #     amount = 1            

            if vesting_amount < 0:
                bank_balances[bank_id] = 0
                auth_accs[auth_id] = 0
                continue

            hmmm += addr + " " + str(vesting_amount)
            bank_balance = bank_balances[bank_id]
        
            SetAmountToBankBalance(bank_balance, vesting_amount + GetAmountFromBankBalance(
                bank_balance
            ))

            auth_vesting_acc = CreateNewVestingAccount(addr, vesting_amount)

            auth_accs[auth_id] = auth_vesting_acc


            n += vesting_amount

            print("modify acc: " + addr + " " + str(vesting_amount))
        
        # new address
        else :
            if vesting_amount < 0:
                continue

            auth_acc = CreateNewVestingAccount(addr, vesting_amount)
            auth_accs.append(auth_acc)

            bank_balance = CreateNewBankBalance(addr, vesting_amount)
            bank_balances.append(bank_balance)
            n += vesting_amount
            print("add new acc: " + addr + " " + str(bank_balance))

    SetBankBalancesForGenesis(genesis, bank_balances)
    SetAuthAccsForGenesis(genesis, auth_accs)
    print("total added coin:", n)
    g.close()
    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)

def NukeAccountsWith1(genesis_dir):
    g = open(genesis_dir, "r")
    genesis = json.load(g)

    auth_accs = GetAuthAccsFromGenesis(genesis)
    bank_balances = GetBankBalancesFromGenesis(genesis)

    auth_accs = [x for x in auth_accs if x != 0]
    bank_balances = [x for x in bank_balances if x != 0]

    SetAuthAccsForGenesis(genesis, auth_accs)
    SetAmountToBankBalance(genesis, bank_balances)

    g.close()
    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)

def NukeAccounts(genesis_dir, nuke_addrs):
    g = open(genesis_dir, "r")
    genesis = json.load(g)

    nuke_addrs = set(nuke_addrs)
    bank_balances = GetBankBalancesFromGenesis(genesis)
    auth_accs = GetAuthAccsFromGenesis(genesis)
    for id, bank_balance in enumerate(bank_balances):
        addr = bank_balance["address"]
        if addr in nuke_addrs:
            bank_balances[id] = 0
            print("nuke acc with addr " + addr)
    for id, auth_acc in enumerate(auth_accs):
        try:
            addr = auth_acc["address"]
            if addr in nuke_addrs:
                auth_accs[id] = 0 
        except:
            addr = auth_acc['base_vesting_account']['base_account']['address']
            if addr in nuke_addrs:
                auth_accs[id] = 0 
    
    auth_accs = [x for x in auth_accs if x != 0]
    bank_balances = [x for x in bank_balances if x != 0]

    SetAuthAccsForGenesis(genesis, auth_accs)
    SetBankBalancesForGenesis(genesis, bank_balances)
    g.close()

    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)
    
def SubstractAccountBalances(genesis_dir, substracting_accs):
    g = open(genesis_dir, "r")
    genesis = json.load(g)

    bank_balances = GetBankBalancesFromGenesis(genesis)

    nuke_addrs = []
    n = 0

    for id, bank_balance in enumerate(bank_balances):
        addr = bank_balance["address"]
        substracting_amount = substracting_accs.get(addr)
        if substracting_amount != None:
            n += substracting_amount
            new_amount = GetAmountFromBankBalance(bank_balance) - substracting_amount
            print("modifying addr " + addr + " to " + str(new_amount))
            if new_amount == 0:
                nuke_addrs.append(addr)
                continue
            SetAmountToBankBalance(bank_balances[id], new_amount)
        
    print("total coin subtracted:", n)
    SetBankBalancesForGenesis(genesis, bank_balances)
    g.close()

    f = open(genesis_dir, "w")
    json.dump(genesis, f, indent=2)

    f.close()
    NukeAccounts(genesis_dir, nuke_addrs)