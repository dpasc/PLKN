import os
import os.path
import pandas as pd
import pg8000
from sqlalchemy import MetaData
from sqlalchemy import Table,Column, Integer,String,Date
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Functions





#Clean data


#Pandas DataFrame
csv = "//home//daman//Projects//plkn//Resources//wow.csv"


data_frame = pd.read_csv(csv)

print(data_frame)

#-------- Configure ORM
#Connect to DB
try:
    engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=False)
    Base = declarative_base()
    conn = engine.raw_connection()
    cursor = conn.cursor()
    print("SQL Alchemy Configured: OK")
except:
    print("SQL Alchemy Configured: Failed")
    raise SystemExit
    
class CatalogRecord(Base):
    __tablename__= 'category_dev_schedule'
    id = Column(Integer, primary_key=True)

    hob = Column(String(40), nullable=False)
    mm = Column(String(40), nullable=False)	
    cm_buyer = Column(String, nullable=False)
    sub_cat_name = Column(String, nullable=False)
    review_type = Column(String, nullable=False)
    sub_date_foodco_products = Column(Date, nullable=True)
    notice_of_probable_delisting = Column(Date, nullable=True)
    suppliers_engagement = Column(Date, nullable=True) 
    final_submission_for_branded = Column(Date, nullable=True)
    info_of_new_and_deleted_lines = Column(Date, nullable=True)
    provide_all_wnas_waf_wpf_to_buyer = Column(Date, nullable=True) 
    visual_planogram_due_to_stores = Column(Date, nullable=False)


#Create Session, Like context in EF
Session = sessionmaker(bind = engine)
session = Session()



#Pull up table 
row_count = session.query(CatalogRecord).count()


print(row_count)
#Check if data has ever been imported

records = data_frame.replace({pd.np.nan: None}, inplace=True)

records = data_frame.to_dict(orient="records")

print(records)



if(row_count < 100):
    #If no: insert all
    session.bulk_insert_mappings(CatalogRecord,records,return_defaults=True,render_nulls=True)
    session.commit()
else: 
    print('bye')


#If yes: compare data for changes






#Replace old data with new




#Close connection 
engine.dispose()





#Print report








