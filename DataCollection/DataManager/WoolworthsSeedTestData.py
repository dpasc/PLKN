from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy import text
import pg8000


engine = create_engine('postgresql+pg8000://plkn:password@localhost:5432/woolworths_db', echo=True)
conn = engine.connect()

i = text("""INSERT INTO category_dev_schedule 
    (hob, mm, cm_buyer, sub_cat_name, review_type, sub_date_foodco_products,
    notice_of_probable_delisting, suppliers_engagement, final_submission_for_branded, 
    info_of_new_and_deleted_lines, provide_all_wnas_waf_wpf_to_buyer, 
    visual_planogram_due_to_stores)
    VALUES
        ('EWAN SHEARER','MARK JONES','MITCHELL GREATOREX','FREEZER - PIZZA','MAJOR','2019-04-22 00:00:00','2019-09-23 00:00:00','2019-10-07 00:00:00','2019-10-21 00:00:00','2019-11-18 00:00:00','2019-11-25 00:00:00','2020-02-10 00:00:00')
        ,('JASON MCQUAID','CHRIS JONES','JUSTIN HEFFERNAN','DAIRY EGGS - OTHER','MAJOR','2019-05-06 00:00:00','2019-10-07 00:00:00','2019-10-21 00:00:00','2019-11-04 00:00:00','2019-12-02 00:00:00','2019-12-09 00:00:00','2020-02-10 00:00:00')
        ,('JASON MCQUAID','CHRIS JONES','JUSTIN HEFFERNAN','DAIRY EGGS - ORGANIC','MAJOR','2019-05-06 00:00:00','2019-10-07 00:00:00','2019-10-21 00:00:00','2019-11-04 00:00:00','2019-12-02 00:00:00','2019-12-09 00:00:00','2020-02-10 00:00:00');
    """)


res = conn.execute(i)



