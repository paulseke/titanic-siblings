# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:04:27 2016

@author: seke
"""

# The following code reads all the Titanic data into 
# Pandas DataFrames.

import pandas as pd
import numpy as np

titanic_df = pd.read_csv('titanic_data.csv')

# The following code displays Titanic data first 5 lines
print titanic_df.head()
print ""

# Checking data types of our data to assess whether the parameters we are interested in
# are available and usable

print titanic_df.dtypes
print ""

# Assessing the presence of missing data (NaN)

titanic_df.isnull().sum()
print ""

# Droping of columns with information not relevant for the study
del titanic_df['Ticket']
del titanic_df['Fare']
del titanic_df['Cabin']
del titanic_df['Name']
del titanic_df['Pclass']
del titanic_df['Sex']
del titanic_df['Parch']
del titanic_df['Embarked']

print titanic_df.head()



