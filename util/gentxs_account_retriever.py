import json
import os

def get_gentxs_account(gentxs_file):
    # read file
    g = open(gentxs_file, "r")
    gentxs = json.load(g)

    addr = gentxs["body"]["messages"][0]["delegator_address"]

    amount = int(gentxs["body"]["messages"][0]["value"]["amount"])*1000

    return addr, amount

def get_seed_account(gentxs_file):
    # get seed
    g = open(gentxs_file, 'r')
    gentxs = json.load(g)

    memo = gentxs["body"]["memo"]

    if memo.split("@")[1].startswith("192.168"):
        return ""

    return memo

def get_gentxs_accounts(gentxs_folder):
    gentxs_accounts = {}

    gentxs_files = os.listdir(gentxs_folder)

    for file in gentxs_files:
        if not file.startswith("gentx"):
            continue
        
        gentxs_file = f"{gentxs_folder}/{file}"
        addr, amount = get_gentxs_account(gentxs_file)

        if addr in gentxs_accounts:
            print(addr, " is duplicate in file ", gentxs_file)
            continue

        gentxs_accounts[addr] = amount
    
    print("total account processing = ", len(gentxs_accounts))
    return gentxs_accounts

def get_seeds(gentxs_folder):
    gentxs_files = os.listdir(gentxs_folder)

    f = open("data/seed.txt", "w")

    for file in gentxs_files:
        if not file.startswith("gentx"):
            continue
        
        gentxs_file = f"{gentxs_folder}/{file}"
        peer = get_seed_account(gentxs_file)

        f.write(peer+'\n')
    
    f.close()