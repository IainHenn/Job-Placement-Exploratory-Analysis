import pandas as pd 
import plotly.express as px

pd.set_option('display.max_columns',None)
JP_df = pd.read_csv("C:/Users/Iaine/.vscode/Python Projects/Job Placement Data + Exploratory Analysis/job_placement.csv")
JP_df = JP_df.rename(columns = {"stream":"major"})
JP_df["college_name"] = JP_df["college_name"].astype("string")
JP_df["gender"] = JP_df["gender"].astype("string")

mean_salaries_per_college_JP_df = JP_df.groupby("college_name")["salary"].mean().sort_values()
print(mean_salaries_per_college_JP_df)

mean_salaries_per_college_JP_df = JP_df.groupby("major")["salary"].mean().sort_values()
print(mean_salaries_per_college_JP_df)

JP_df["gender"] = JP_df["gender"].replace("Male","M")
JP_df["gender"] = JP_df["gender"].replace("Female","F")
