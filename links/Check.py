from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query

engine = create_engine('sqlite:///C:/DB/test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
from sqlalchemy import MetaData
meta = MetaData()
#meta.drop_all(engine)
astra = []
syu = Table(
   'UrlLinks', meta,
   Column('id', Integer, primary_key = True),
   Column('Branch', String),
   Column('URLLinks', String),
   Column('Time', String),

)

meta.create_all(engine)
# s = ("SELECT URLLinks FROM UrlLinks GROUP BY URLLinks" )

# result = conn.execute(s)
# for raw in result:
#    astra.append(s)

s = [
"/domain-theft-recovery",
"/get-domain-score",
"/legal/about-dnp-score",
"/legal/affiliate",
"/legal/contact",
"/legal/copyright",
"/legal/disclaimer",
"/legal/end-user-privacy-terms",
"/legal/end-user-terms-and-conditions",
"/legal/how-it-works",
"/legal/insurance-conditions",
"/legal/sample-domain-name-ownership-coverage-policy",
"/legal/support",
"/protect-a-domain",
"/stolen-domains"

]

devRecoveryTheft = ("SELECT AVG(TIME) FROM UrlLinks WHERE URLlinks ="+"domain-theft-recovery")
conn = engine.connect()
resultdevRecoveryTheft = conn.execute(devRecoveryTheft)
print(resultdevRecoveryTheft)


