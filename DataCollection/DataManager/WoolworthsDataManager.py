import os
import os.path
import pandas as pd
import pg8000
from sqlalchemy import MetaData
from sqlalchemy import Table,Column, Integer,String,Date
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#File path
csv_file = "//home//daman//Projects//plkn//Resources//wow.csv"

#See if file is there
if os.path.isfile(csv_file):
    print("CSV Found")

else:
    print("CSV Not Found")
    raise SystemExit


#Get data
pd.set_option('display.max_rows',None)
data = pd.read_csv(csv_file, header=5)


print(data)

#Clean Dataobject
column_names = {
    'HOB':'hob',
    'MM':'mm',	
    'CM / Buyer':'cm_buyer',
    'Sub-Category Name':'sub_cat_name',
    'Review Type':'review_type',
    'Submission date for FoodCo Own Brand Products':'sub_date_foodco_products',
    '"Notice of Probable Delisting" letter sent to impacted suppliers':'notice_of_probable_delisting',
    'Supplier engagement:\nSubmissions opened for review & Supplier recommendations for deletions\n':'suppliers_engagement',
    'Final submission date for Branded Products':'final_submission_for_branded',
    'Results to Suppliers of New & Deleted Lines\n\n"Notice of Final Delisting" letter sent to impacted suppliers':'info_of_new_and_deleted_lines',	
    'Suppliers to provide all WNAS, WAF, WPF to Buyer':'provide_all_wnas_waf_wpf_to_buyer',
    'VISUAL PLANOGRAM DUE TO STORES':'visual_planogram_due_to_stores'
}

data.rename(columns= column_names, inplace =True)


#Connect to DB


engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=False)
Base = declarative_base()
'''    print("Database Connection:OK")
except:
    print("Database Connection:Failed")
    raise SystemExit'''


    
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

#Check if data has ever been imported

if(row_count < 1):
    #If no: insert all
    print("heelo")
    
else:
    print("bye")


#If yes: compare data for changes






#Replace old data with new




#Close connection 
engine.dispose()





#Print report








