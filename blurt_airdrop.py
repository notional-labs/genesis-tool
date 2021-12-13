import bech32

import binascii
import csv

fDir = "blurt_airdrop.csv"

total = 23692868 * 1e6

def get_blurts():
    total_blurts = 0
    blurt_maps = {}
    with open(fDir, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader :
            blurt_maps[rows[0]] = rows[1]
            total_blurts += float(rows[1])

    sum = 0

    m = {}
    for addr, balance in blurt_maps.items() :
        addr = addr.strip().lower()
        _, addrBz = bech32.bech32_decode(addr)
        addr = bech32.bech32_encode('dig',addrBz)

        b = float(balance) * total / total_blurts

        m[addr] = int(b)

        sum += b

    print("total airdrop amount for blurt: ", sum)
    
    return m

get_blurts()     
        
