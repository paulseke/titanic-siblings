# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:14:50 2016

@author: seke
"""
# Some useful functions
# This function compares two proportions given two values in the same category
from scipy import stats
def proportion_comparator_for_one_df_row(given_np_row):
    matrix_builder = np.array([[dead_pd_series_3_groups.sum(),given_np_row[0]], 
                          [survivors_pd_series_3_groups.sum(),given_np_row[1]]])
    return  stats.chi2_contingency(matrix_builder)


# This function compares proportions row-wise along the dataframe
def proportion_comparator(siblings_number_df):
    return siblings_number_df.apply(proportion_comparator_for_one_df_row, axis=1) # passes an object row-wise
    
# Running the functions
print proportion_comparator(siblings_number_df_3_groups)

