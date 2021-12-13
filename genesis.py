import genesis_util

# import blurt_airdrop
import dfy_airdrop
import genesis_util
import nuke_accs
import dig_sale
import blurt_airdrop
import ion_airdrop
import old_validator_airdrop

dir = "genesis.json"

# nuke accs

# nukes = nuke_accs.get_nuke_accs()
# genesis_util.NukeAccounts(dir, nukes)


# convert

# airdrop = dfy_airdrop.get_dfy_airdrop()
# genesis_util.ConvertAuthBaseAccountsToVestingAccounts("genesis.json", airdrop)



# add new vesting accs

# total air drop for blurt 23692868000000.008 udig
# blurt = blurt_airdrop.get_blurts()
# genesis_util.AddVestingAccountsIntoGenesis("genesis.json", blurt)

# ion = ion_airdrop.get_ions()
# genesis_util.AddVestingAccountsIntoGenesis("genesis.json", ion)

# validator = old_validator_airdrop.get_old_validators_airdrop()
# genesis_util.AddVestingAccountsIntoGenesis("genesis.json", validator)

# notional = {"dig1msezx0rywmz2x3ewhzusfpuf5env5deg5erw63": 62385737000000}
# genesis_util.AddVestingAccountsIntoGenesis(dir, notional)

# add new non-vesting accs

# reverse = dig_sale.GetReserve()
# genesis_util.AddAccountsIntoGenesis("genesis.json", reverse)

# liquidity_boostrapping = {"dig13qxgtvk3ttjfygm7qk4ftd8yvz63qv5zx6tuq6": 47385737000000}
# genesis_util.AddAccountsIntoGenesis(dir, liquidity_boostrapping)

# validator_treasury = {"dig1880q0w9dzt439fgmwslvaur7pq6jv0fzx4zx0a": 71078605000000}
# genesis_util.AddAccountsIntoGenesis(dir, validator_treasury)

# sale = dig_sale.GetSaleMap()
# genesis_util.AddAccountsIntoGenesis("genesis.json", sale)

founder = dig_sale.GetFounders()
genesis_util.AddAccountsIntoGenesis(dir, founder)