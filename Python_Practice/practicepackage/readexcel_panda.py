import pandas as pd

def readexcel():
    r = pd.read_excel("trainlist_updated.xlsx")
    for items in r.iterrows():
        with open('read.txt', 'a') as w:
           # w.write(str(items))
            w.writelines(str(items))

readexcel()