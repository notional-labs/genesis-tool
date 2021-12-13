import genesis_util

# import blurt_airdrop
import dfy_airdrop
import genesis_util
import nuke_accs
import dig_sale
import blurt_airdrop
import ion_airdrop

dir = "genesis.json"

# nukes = nuke_accs.get_nuke_accs()
# genesis_util.NukeAccounts(dir, nukes)

# airdrop = dfy_airdrop.get_dfy_airdrop()

# genesis_util.VestingAccountsIntoGenesis("genesis.json", airdrop)

# sale = dig_sale.GetSaleMap()

# genesis_util.AddAccountsIntoGenesis("genesis.json", sale)

# total air drop for blurt 23692868000000.008 udig
# blurt = blurt_airdrop.get_blurts()
# genesis_util.AddVestingAccountsIntoGenesis("genesis.json", blurt)

ion = ion_airdrop.get_ions()
genesis_util.AddVestingAccountsIntoGenesis("genesis.json", ion)
