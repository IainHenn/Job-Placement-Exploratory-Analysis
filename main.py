import pandas as pd 
import plotly.express as px
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_recall_curve
import numpy as np

#pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows', None)
JP_df = pd.read_csv("C:/Users/Iaine/.vscode/Python Projects/Job Placement Data + Exploratory Analysis/job_placement.csv")
JP_df = JP_df.rename(columns = {"stream":"major"})
JP_df["college_name"] = JP_df["college_name"].astype("string")
JP_df["gender"] = JP_df["gender"].astype("string")
print(JP_df.dtypes)
#Setting Up The Data To be Messed With 


JP_df["gender"] = JP_df["gender"].replace("Male","M")
JP_df["gender"] = JP_df["gender"].replace("Female","F")
#Changing "Male" to "M" and "Female" to "F" for simplicity and to make the data look cleaner 

jp_dupe = JP_df.duplicated()
print(jp_dupe[jp_dupe == "True"])
#There's no duplicates in the data 

#print(JP_df.groupby("name").count())
#It seems like data used random names to keep anonymity, the name column means nothing to the data 

JP_df_noName = JP_df.drop("name", inplace = False, axis = 1)
#print(JP_df_noName)

#print(JP_df_noName["degree"].unique())
#everyone has a bachelor's degree in this data set, dropping it 
JP_df_noName_noDegree = JP_df_noName.drop("degree",inplace = False, axis = 1)
#print(JP_df_noName_noDegree)

#Replace NAN values 
JP_df_noName_noDegree = JP_df_noName_noDegree.fillna(0)

#Feature Encoding****
#Need to convert categorical variables to a numeric format (i.e. gender, major, and college_name)
print(JP_df_noName_noDegree)

#gender feature encoded 
JP_df_cleaned = JP_df_noName_noDegree 
JP_df_cleaned["gender"] = JP_df_cleaned["gender"].replace("M","1")
JP_df_cleaned["gender"] = JP_df_cleaned["gender"].replace("F","0")
JP_df_cleaned["gender"] = JP_df_cleaned["gender"].astype("int")

#major feature encoded 
# 1 - (CS), 2 - (EE), 3 - (E&C), 4 - (IT), 5 - (ME)
JP_df_cleaned["major"] = JP_df_cleaned["major"].replace("Computer Science","1")
JP_df_cleaned["major"] = JP_df_cleaned["major"].replace("Electrical Engineering","2")
JP_df_cleaned["major"] = JP_df_cleaned["major"].replace("Electronics and Communication","3")
JP_df_cleaned["major"] = JP_df_cleaned["major"].replace("Information Technology","4")
JP_df_cleaned["major"] = JP_df_cleaned["major"].replace("Mechanical Engineering","5")
JP_df_cleaned["major"] = JP_df_cleaned["major"].astype("int")

#college_name feature encoded
print(JP_df_cleaned["college_name"].nunique())
unique_colleges = JP_df_cleaned["college_name"].unique()
for i in range(0,JP_df_cleaned["college_name"].nunique()):
    JP_df_cleaned["college_name"] = JP_df_cleaned["college_name"].replace(unique_colleges[i],str(i+1))


#placement_status feature encoded 
JP_df_cleaned["placement_status"] = JP_df_cleaned["placement_status"].replace("Placed","1")
JP_df_cleaned["placement_status"] = JP_df_cleaned["placement_status"].replace("Not Placed","0")



#features 
#no gender or college name or major
feature_columns = np.array(["age","gender","major","college_name","gpa","years_of_experience"])
X = JP_df_noName_noDegree[feature_columns]
#target
Y = JP_df_noName_noDegree.placement_status

selector = SelectKBest(chi2,k = 5)
X_new = selector.fit_transform(X,Y)
print(selector.get_support())

X_train, X_test, Y_train, Y_test = train_test_split(X_new,Y,test_size = .25, train_size = .75)

logReg = LogisticRegression()
logReg.fit(X_train,Y_train)

Y_predicted = logReg.predict(X_test)

target_names = ["Placed","Not Placed"]
print(classification_report(Y_test,Y_predicted, target_names = target_names))
