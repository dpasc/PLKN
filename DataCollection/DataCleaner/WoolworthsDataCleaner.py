import os
import os.path
import pandas as pd


#File path
file_path = "//home//daman//Projects//plkn//Resources//"
xlsx =file_path+"wow.xlsx"
csv = file_path +"wow.csv"


#Convert to CSV
data_xls = pd.read_excel(xlsx)
data_xls.to_csv(file_path + "wow.csv", index=False)

#Delete XLSX File
os.remove(xlsx)

#See if file is there
if os.path.isfile(csv):
    print("CSV Found")

else:
    print("CSV Not Found")
    raise SystemExit


#Get data
pd.set_option('display.max_rows',None)
data_frame = pd.read_csv(csv, header=5)




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
#Set new names for columns
data_frame.rename(columns= column_names, inplace =True)


#Delele old CSV
os.remove(csv)


#Save new Clean file
data_frame.to_csv(csv,index=False, header = True)


print(data_frame)

