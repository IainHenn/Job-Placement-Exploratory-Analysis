import pandas as pd 
import plotly.express as px

pd.set_option('display.max_columns',None)
JP_df = pd.read_csv("C:/Users/Iaine/.vscode/Python Projects/Job Placement Data + Exploratory Analysis/job_placement.csv")
JP_df = JP_df.rename(columns = {"stream":"major"})
JP_df["college_name"] = JP_df["college_name"].astype("string")
JP_df["gender"] = JP_df["gender"].astype("string")
#Setting Up The Data To be Messed With 


JP_df["gender"] = JP_df["gender"].replace("Male","M")
JP_df["gender"] = JP_df["gender"].replace("Female","F")
#Changing "Male" to "M" and "Female" to "F" for simplicity and to make the data look cleaner 

jp_dupe = JP_df.duplicated()
print(jp_dupe[jp_dupe == "True"])
#There's no duplicates in the data 

mean_salaries_per_college_JP_df = JP_df.groupby("college_name")["salary"].mean().sort_values()
print(mean_salaries_per_college_JP_df)
#Average salary per college 

mean_salaries_per_college_JP_df = JP_df.groupby("major")["salary"].mean().sort_values()
print(mean_salaries_per_college_JP_df)
#Average salary per major 

#for i in range(len(JP_df)):
    #if(JP_df.iloc[i]["salary"] == 0):
        #JP_df.drop(i)

#print(JP_df.loc[JP_df["salary"] == 0])

#salaries_fig = px.histogram(JP_df,x = "salary")
#salaries_fig.show()
#Creating a histogram that is a histogram of the salaries and the counts of the salaries 