import os
from dotenv import load_dotenv
load_dotenv()

import util.bech32_airdrop as bech32_airdrop
import util.genesis_util as genesis_util
import util.gentxs_account_retriever as gentxs_account_retriever

prefix = os.getenv("ACC_PREFIX")

# blurt_total = 1.5*1e6
# 
# def blurt_airdrop_algo(balance, total_snapshot_coin):
    # return float(balance)*(blurt_total/total_snapshot_coin)
# 
# accs = bech32_airdrop.get_converted_airdrop_snapshot(
    # prefix, 
    # "data/anone_blurt_airdrop.csv",
    # blurt_airdrop_algo
    # )

# add vesting account into genesis
# genesis_util.AddVestingAccountsIntoGenesis("data/genesis.json", accs)

# accs = gentxs_account_retriever.get_gentxs_accounts("data/gentx")

# genesis_util.AddAccountsIntoGenesis("data/genesis.json", accs)

gentxs_account_retriever.get_seeds("data/gentx")