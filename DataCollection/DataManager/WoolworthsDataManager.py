import os
import os.path
import pg8000
import pandas as pd
import numpy as np
from sqlalchemy import Table,Column,Integer,String,Date,create_engine,func,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Function(s)

# move this function to date cleaner
def date_formatter(data_frame):
    data_frame['sub_date_foodco_products'] = pd.to_datetime(data_frame.sub_date_foodco_products)
    data_frame['notice_of_probable_delisting'] = pd.to_datetime(data_frame.notice_of_probable_delisting)
    data_frame['suppliers_engagement'] = pd.to_datetime(data_frame.suppliers_engagement)
    data_frame['final_submission_for_branded'] = pd.to_datetime(data_frame.final_submission_for_branded)
    data_frame['info_of_new_and_deleted_lines'] = pd.to_datetime(data_frame.info_of_new_and_deleted_lines)
    data_frame['provide_all_wnas_waf_wpf_to_buyer'] = pd.to_datetime(data_frame.provide_all_wnas_waf_wpf_to_buyer)
    data_frame['visual_planogram_due_to_stores'] = pd.to_datetime(data_frame.visual_planogram_due_to_stores)

#Close database connection and exit script
def close_connection_and_exit(engine):
    if(engine):
        engine.dispose
    raise SystemExit

#Pandas DataFrame
csv = "//home//daman//Projects//plkn//Resources//wow.csv"
data_frame = pd.read_csv(csv)

#-------- Configure ORM
#Connect to DB
try:
    engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=False)
    Base = declarative_base()
    conn = engine.raw_connection()
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


#Check if data has ever been imported
if(row_count < 1):
    #If no: insert all
    records = data_frame.replace({np.nan: None}, inplace=True)
    records = data_frame.to_dict(orient="records")
    print(records)
    # This needs to work
    session.bulk_insert_mappings(CatalogRecord,records,return_defaults=True,render_nulls=False)
    session.commit()
    close_connection_and_exit(engine)

else: 
    #Pull out data from database into a new dataframes
    db_data_frame= pd.read_sql_table('category_dev_schedule',con=engine)
    date_formatter(data_frame)
                        
#Prepare dataframes
updated_data = db_data_frame.merge(data_frame, how='outer', indicator=True).loc[lambda x : x['_merge']=='right_only']
data_to_remove = db_data_frame.merge(data_frame, how='outer', indicator=True).loc[lambda x : x['_merge']=='left_only']


#Check to see if there is new data
#If yes: compare data for changes
if( len(updated_data.index) > 0):
    #Remove old data
    for key,value in data_to_remove['id'].iteritems():
        item_to_delete = session.query(CatalogRecord).get(value)
        session.delete(item_to_delete)
    
    #Add new
    del updated_data['id']
    del updated_data['_merge']
    del updated_data['date_added']
    updated_data.to_sql("category_dev_schedule", con=engine,if_exists='append', index=False)
    #Commit changes
    session.commit()

#Print report
close_connection_and_exit(engine)






