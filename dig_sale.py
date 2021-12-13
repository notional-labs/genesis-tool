import pandas as pd


sale_file_dir = "sale_map.xlsx"
reverse_dir = "reserve.xlsx"

def ReadExcelFile(file_dir):
    xls = pd.ExcelFile(file_dir)

    dfs = list(pd.read_excel(xls, sheet_name=None).values())

    accounts_map = {}
    sum = 0 
    for df in dfs:
        for _,r in df.iterrows():
            
            try :
                account_add = r[2].strip().lower()
                if account_add[:4] == "dig1" or account_add[:2] == "0x":
                    if accounts_map.get(account_add) != None:
                        accounts_map[account_add] += int(r[3] * 1e6)
                    else:
                        accounts_map[account_add] = int(r[3] * 1e6)
            except:
                continue
    for _, amount in accounts_map.items():
        sum += amount
    print("total sale of dig:", sum)
    return accounts_map

def GetSaleMap():
    return ReadExcelFile(sale_file_dir)

def GetReserve():
    return ReadExcelFile(reverse_dir) 

print(GetSaleMap())


