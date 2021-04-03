import os
import pandas as pd

def dumpTanuki(tanuki):
    df_lst = []
    for n, table in enumerate(tanuki):
        df = pd.DataFrame({"id":table.id,
                            "name":table.name,
                            "age":table.age,
                            "type":table.type},
                            index=[n])
        df_lst.append(df)
    df = pd.concat(df_lst)

    return df
    #df.to_csv("results/TransportNumber.csv", index=False)
