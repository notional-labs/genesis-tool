import bech32

import csv

fDir = "old_validator_airdrop.csv"


def get_old_validators_airdrop():
    acc_map = {}
    with open(fDir, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader :
            print(rows)
            acc_map[rows[0]] = rows[1]
    sum = 0

    m = {}
    for addr, balance in acc_map.items() :
        addr = addr.strip().lower()
        _, addrBz = bech32.bech32_decode(addr)
        addr = bech32.bech32_encode('dig',addrBz)

        b = float(balance) * 1e6

        m[addr] = int(b)

        sum += b

    print("total airdrop amount for old validator: ", sum)
    
    return m

get_old_validators_airdrop()

        