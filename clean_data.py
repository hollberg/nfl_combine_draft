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
#print(df_colleges.head())
#print(df_colleges.shape)


def group_imputer(df, grouping_col, cols_to_impute):
    """
    Impute values in a dataframe based on averages WITHIN a given category
    :param df: Pandas DataFrame
    :param grouping_col: String, column name to group by
    :param cols_to_impute: List, column names where NaNs will be imputed
    :return: Pandas DataFrame
    """
    entries_in_group_col = df[grouping_col].unique()
    df_group_means = df.groupby(by=grouping_col)[cols_to_impute].median()

    # Loop over input df and replace/impute values
    for entry in entries_in_group_col:
        for column in cols_to_impute:
            fill_value = df_group_means.loc[entry, column]
            # fill_value = 100.01
            # df[df[grouping_col]==entry][column] = df[df[grouping_col]==entry][column].fillna(fill_value)
            # df[df[grouping_col] == entry][column].fillna(fill_value, inplace=True)
            mask = df[grouping_col] == entry
            df.loc[mask, column] = df.loc[mask, column].fillna(fill_value)

    return df


# df = df_combine
# grouping_col = 'pos'
# cols_to_impute = ['height (in)', 'weight (lbs)', 'hand size (in)', 'arm length (in)',
#                   '40 yard', 'bench press', 'vert leap (in)', 'broad jump (in)',
#                   'shuttle', '3cone', '60yd shuttle']
#
# entries_in_group_col = df[grouping_col].unique()
#
# df_group_means = df.groupby(by=grouping_col)[cols_to_impute].median()
#
# # Loop over input df and replace/impute values
# for entry in entries_in_group_col:
#     for column in cols_to_impute:
#         fill_value = df_group_means.loc[entry, column]
#         # fill_value = 100.01
#         # df[df[grouping_col]==entry][column] = df[df[grouping_col]==entry][column].fillna(fill_value)
#         # df[df[grouping_col] == entry][column].fillna(fill_value, inplace=True)
#         mask = df[grouping_col]==entry
#         df.loc[mask, column] = df.loc[mask, column].fillna(fill_value)
#
#
# df.to_clipboard()
moo='boo'

