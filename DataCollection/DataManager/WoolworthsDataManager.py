import os
import os.path
import pandas as pd
import numpy as np
import pg8000
from sqlalchemy import MetaData
from sqlalchemy import Table,Column, Integer,String,Date
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Functions


def dataframe_difference(df1, df2, which=None):
    #Find rows which are different between two data frames
    comparison_df = df1.merge(df2,indicator=True,how='outer')
    
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    return diff_df


#Clean data

#Pandas DataFrame
csv = "//home//daman//Projects//plkn//Resources//wow.csv"
data_frame = pd.read_csv(csv)

#-------- Configure ORM
#Connect to DB
try:
    engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=True)
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


if(row_count < 1):
    #If no: insert all
    records = data_frame.replace({np.nan: None}, inplace=True)
    records = data_frame.to_dict(orient="records")
    session.bulk_insert_mappings(CatalogRecord,records,return_defaults=True,render_nulls=True)
    session.commit()
else: 
    #Pull out data from database into a new dataframe
    db_data_frame= pd.read_sql_table('category_dev_schedule',con=engine)
    del db_data_frame['id']
    
    #Compare data
    #Concat method
    
    updated_data = pd.concat([data_frame,db_data_frame]).drop_duplicates(keep=False)

'''
    updated_data = updated_data.reset_index(drop=True)

    updated_data_gpby = updated_data.groupby(list(updated_data.columns))
    idx = [x[0] for x in updated_data_gpby.groups.values() if len(x) !=1]

    updated_data.reindex(idx)
    

    updated_data = dataframe_difference(db_data_frame,data_frame)'''

print("CSV DATA===================================================================================")
print(data_frame)
print("DB DATA===================================================================================")
print(db_data_frame)
print("UPDATED===================================================================================")
print(updated_data)
updated_data.to_csv('//home//daman//Projects//plkn//DataCollection//DataManager//udf.csv', header=True, index=None, sep=',')
    #Make changes to 
                        


#If yes: compare data for changes




#Replace old data with new




#Close connection 
engine.dispose()





#Print report








