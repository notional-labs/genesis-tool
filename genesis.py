import genesis_util

# import blurt_airdrop
import dfy_airdrop
import genesis_util

airdrop = dfy_airdrop.get_dfy_airdrop()
print(airdrop)

genesis_util.ConvertAuthBaseAccountsToVestingAccounts("genesis.json", airdrop)

# genesis_util.VestingAccountsIntoGenesis("genesis.json", airdrop)
