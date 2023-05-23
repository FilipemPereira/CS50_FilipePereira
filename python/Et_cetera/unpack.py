
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts":25}

# unpack coin list to total arguments
print(total(*coins), "Knuts") 

# unpack coin dictionary to total arguments
print(total(**coins), "Knuts") 
