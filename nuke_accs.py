def get_nuke_accs():
    f = open("nuke_acc", "r")
    nuke_accs = f.read().split('\n')
    return nuke_accs