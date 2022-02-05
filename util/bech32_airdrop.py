import bech32
import csv

def get_converted_airdrop_snapshot(prefix, snapshot_file, airdrop_algo):
    total_snapshot_coin = 0
    snapshot_maps = {}
    
    # get total amount of coin in snapshot
    with open(snapshot_file, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader :
            snapshot_maps[rows[0]] = rows[1]
            total_snapshot_coin += float(rows[1])

    sum = 0

    converted_airdrop_snapshot = {}
    for addr, balance in snapshot_maps.items() :
        # convert whatever type to prefix type
        addr = addr.strip().lower()
        _, addrBz = bech32.bech32_decode(addr)

        addr = bech32.bech32_encode(prefix,addrBz)

        # airdrop algorithm to determint amount of airdrop
        amount_per_addr = airdrop_algo(balance, total_snapshot_coin)

        converted_airdrop_snapshot[addr] = round(amount_per_addr)

        sum += converted_airdrop_snapshot[addr]

    print("total airdrop amount for blurt: ", sum)
    
    return converted_airdrop_snapshot