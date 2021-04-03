"""Register thermal expansion data."""
import pandas as pd
import sqlalchemy.sql.functions as func
from setting import session
from create_db import *

def main():
    df = pd.DataFrame({"id":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       "name":[
                       "ポンタ", 
                       "たぬまる",
                       "たぬ子",
                       "タヌ太郎",
                       "たぬ次郎",
                       "タヌキチ",
                       "たぬ三郎",
                       "たぬ衛門",
                       "ぽん助",
                       "アライグマ"
                       ],
                       "age":[5, 3, 8, 4, 5, 8, 1, 5, 9, 10],
                       "type":[
                       "ウスリータヌキ",
                       "タイリクタヌキ",
                       "エゾタヌキ",
                       "ホンドタヌキ",
                       "コウライタヌキ",
                       "ホンドタヌキ",
                       "ウスリータヌキ",
                       "エゾタヌキ",
                       "ホンドタヌキ",
                       "アライグマ"
                       ]
                       })
    session.bulk_save_objects([Tanuki(id=int(df["id"][i]),
                               name=df["name"][i],
                               age=int(df["age"][i]),
                               type=df["type"][i])
                               for i in range(len(df))])
    
    session.commit()

if __name__ == "__main__":
    main()
