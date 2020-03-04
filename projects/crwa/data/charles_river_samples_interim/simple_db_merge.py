# This file
import numpy as np
import pandas as pd

import os
import datetime
import sys

data_dir = "../charles_river_samples_csv/"

# Construct a dictionary of DataFrames, keyed on the filename
df_dict = {file[:-4]:pd.read_csv(data_dir+file, encoding="latin-1") for file in os.listdir(data_dir)}


# Process the date/time columns to datetime
results = df_dict["Results"]

results["Time_Collected"] = pd.to_datetime(results["Time_Collected"])
results["Time_Collected"] = results["Time_Collected"].dt.time


# The columns we are using to join are
dfs_to_join = [
    "Data_Type",
    "Media_Type",
    "Media_Subdivision",
    "Component",

    "Activity_Type",
    "Actual_Result_Type",
    "Reporting_Result_Type",
    "Relative_Depth",
]

left_cols_to_join = [
    "Data_Type_ID",
    "Media_Type_ID",
    "Media_Subdivision_ID",
    "Component_ID",

    "Activity_Type_ID",
    "Actual_Result_Type_ID",
    "Reporting_Result_Type_ID",
    "Relative_Depth_ID",
]

right_cols_to_join = [
    "Data_Type_ID",
    "Media_Type_ID",
    "Media_Subdivision_ID",
    "Component_ID",

    "Activity_Type_ID",
    "Result_Type_ID",
    "Result_Type_ID",
    "Relative_Depth_ID",
]

# Do the joins
for left_col, right_col, df_name in zip(left_cols_to_join, right_cols_to_join, dfs_to_join):
    results = results.merge(df_dict[df_name], left_on=left_col, right_on=right_col)

results.drop(columns=left_cols_to_join, inplace=True)

results.to_csv("results_merged.csv",index=False)
