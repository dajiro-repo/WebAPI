from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# AWS 使用時用
# DATABASE = 'postgresql'
# USER = 'postgres'
# PASSWORD = 'postgres'
# HOST = 'database-1.c6nrmuuykz5h.us-east-2.rds.amazonaws.com'
# PORT = '5431'
# DB_NAME = 'animal_db'

# DATABASE = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

#データベースの名前はここで定義
DATABASE = 'sqlite:///tanuki.sqlite3'

#Engine(PythonをSQLに変換)を定義
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
session=SessionClass()

#ベースクラスを作成。データベースモデルはこれを継承する。
Base=declarative_base()
#Base.query = session.query_property()
