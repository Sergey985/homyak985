from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query

engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
from sqlalchemy import MetaData
meta = MetaData()
#meta.drop_all(engine)

syu = Table(
   'UrlLinks', meta,
   Column('id', Integer, primary_key = True),
   Column('Branch', String),
   Column('URLLinks', String),
   Column('Time', String),

)

meta.create_all(engine)
# ins = syu.insert().values(Branch = 'Dev', URLLinks = 'www.host.com/seno', Time = '12:12:12 09.09.09')
# con = engine.connect()
# result = con.execute(ins)
#
# s = syu.select()
# conn = engine.connect()
# result = conn.execute(s)
# for raw in result:
#       print(raw)