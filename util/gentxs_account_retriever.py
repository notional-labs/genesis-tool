import json
import os

def get_gentxs_account(gentxs_file):
    # read file
    g = open(gentxs_file, "r")
    gentxs = json.load(g)

    addr = gentxs["body"]["messages"][0]["delegator_address"]

    amount = int(gentxs["body"]["messages"][0]["value"]["amount"])*1000

    return addr, amount

def get_gentxs_accounts(gentxs_folder):
    gentxs_accounts = {}

    gentxs_files = os.listdir(gentxs_folder)
    for file in gentxs_files:
        if not file.startswith("gentx"):
            continue
        
        gentxs_file = f"{gentxs_folder}/{file}"
        addr, amount = get_gentxs_account(gentxs_file)
        gentxs_accounts[addr] = amount
    
    return gentxs_accounts