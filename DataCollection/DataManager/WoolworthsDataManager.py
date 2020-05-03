import os
import os.path
import pandas as pd
import pg8000
from sqlalchemy import MetaData
from sqlalchemy import Table,Column, Integer,String,Date
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Connect to DB
try:
    engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=False)
    Base = declarative_base()
    print("Database Connection:OK")
except:
    print("Database Connection:Failed")
    raise SystemExit


    
class CatalogRecord(Base):
    __tablename__= 'category_dev_schedule'
    id = Column(Integer, primary_key=True)

    hob = Column(String(40))
    mm = Column(String(40))	
    cm_buyer = Column(String)
    sub_cat_name = Column(String)
    review_type = Column(String)
    sub_date_foodco_products = Column(Date)
    notice_of_probable_delisting = Column(Date)
    suppliers_engagement = Column(Date) 
    final_submission_for_branded = Column(Date)
    info_of_new_and_deleted_lines = Column(Date)
    provide_all_wnas_waf_wpf_to_buyer = Column(Date) 
    visual_planogram_due_to_stores = Column(Date)


#Create Session, Like context in EF
Session = sessionmaker(bind = engine)
session = Session()

#Pull up table 
row_count = session.query(CatalogRecord).count()


print(row_count)
#Check if data has ever been imported




if(row_count < 1):
    #If no: insert all
    try:
         data_frame.to_sql(
        name='category_dev_schedule',
        con=engine, 
        if_exists='replace',
        index = False
        )
    except:

        engine.dispose()
        raise SystemExit
    
else: 
    print('bye')


#If yes: compare data for changes






#Replace old data with new




#Close connection 
engine.dispose()





#Print report








