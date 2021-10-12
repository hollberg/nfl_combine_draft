"""
clean_data.py

Clean up raw *.csv files
"""


# Imports
import numpy as np
import pandas as pd
combine_file = r'data\nfl_combine_1987_2020.csv'

df_raw_combine = pd.read_csv(combine_file)

df_raw_combine.head()

draft_file = r'data\espn_draft_history_2000_2021_cleaned.csv'
df_raw_draft = pd.read_csv(draft_file)

df_draft = df_raw_draft

df_draft.columns = df_draft.columns.str.lower()
df_draft.columns

combine_cols_to_drop = ['Unnamed: 0', 'Wonderlic']
df_combine = df_raw_combine
df_combine.drop(columns=combine_cols_to_drop, inplace=True)
df_combine.columns = df_combine.columns.str.lower()
df_combine.head()

df_colleges = df_combine.merge(df_draft, how='inner', left_on='college', right_on='school')
print(df_colleges.head())
print(df_colleges.shape)


