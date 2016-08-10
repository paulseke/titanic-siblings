# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:20:40 2016

@author: seke
"""

# More data munging
# Resetting row index
age_df_no_nan = age_df_no_nan.reset_index(drop=True)

# Age equal to zero
print age_df_no_nan[(age_df_no_nan['Age'] == 0)]
print ""

# Age between 0 and 1
print age_df_no_nan[(age_df_no_nan['Age'] < 1) & (age_df_no_nan['Age'] > 0)]
print ""

# Replacing typos 0.x with their value x 
# this method also add value 100 to Siblings column. Will be nullified in further steps by using >0
# instead of == 1 while selecting data (see age_data_parser_survivors function below)
age_df_no_nan[(age_df_no_nan['Age'] < 1) & (age_df_no_nan['Age'] > 0)] = 100*(age_df_no_nan[(age_df_no_nan['Age'] < 1) & (age_df_no_nan['Age'] > 0)])

# Verifying that typos were removed
print age_df_no_nan[(age_df_no_nan['Age'] < 1) & (age_df_no_nan['Age'] > 0)]
print ''
print age_df_no_nan['Age'].iloc[59]
print age_df_no_nan['Age'].iloc[243]
print age_df_no_nan['Age'].iloc[374]

def checking_typos (age_df_no_nan):
    for i in range (len(age_df_no_nan)):
        return age_df_no_nan[age_df_no_nan[(age_df_no_nan['Age'] < i+1) & (age_df_no_nan['Age'] > i)] != 0]

# Assessing the number of typos remaining (assuming that age in years is an integer)
print (checking_typos (age_df_no_nan).isnull().sum()[['Age']]) - len(age_df_no_nan)                   
                       
 # Getting the age of survivors and the number of siblings
age_no_nan_survived = age_df_no_nan[age_df_no_nan['Survived'] > 0]#
# Resetting row index
age_no_nan_survived = age_no_nan_survived.reset_index(drop=True)

# Getting the age of survivors and the number of siblings
age_no_nan_died = age_df_no_nan[age_df_no_nan['Survived'] == 0]
# Resetting row index
age_no_nan_died = age_no_nan_died.reset_index(drop=True)

# Making sure than both groups have a high number of values
print age_no_nan_survived.head()
print ''
print 'number of survivor values available:', age_no_nan_survived['Age'].count()
print 'number of dead values available:', age_no_nan_died['Age'].count()                      