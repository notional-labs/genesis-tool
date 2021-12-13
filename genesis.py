import genesis_util

# import blurt_airdrop
import dfy_airdrop
import genesis_util
import nuke_accs

dir = "genesis.json"

airdrop = dfy_airdrop.get_dfy_airdrop()
nukes = nuke_accs.get_nuke_accs()

genesis_util.NukeAccounts(dir, nukes)

# genesis_util.VestingAccountsIntoGenesis("genesis.json", airdrop)
