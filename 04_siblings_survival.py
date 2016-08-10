# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:17:37 2016

@author: seke
"""

#  Study of the correlation between the passengers' sibling number aboard, the age and survival
# Verification of the availability of the data of interest
print titanic_df.head()
print ''
print titanic_df.isnull().sum()
print ""

# Copying data to avoid affecting titanic_df eventually
# titanic_df kept for fast comparison, should the necessity emerge
age_df = titanic_df.copy(deep=True) 

# Dropping axis labels with missing data
age_df_no_nan = age_df.dropna()

# Assessessment of the success of missing data removal
print age_df_no_nan.isnull().sum()
print ""
print age_df_no_nan.head()
print ""

# Average number of passengers who survived or died grouped according to their number of siblings aboard and age
age_no_nan_grouped = age_df_no_nan.groupby(['Survived','SibSp','Age'], as_index=True)['PassengerId'].count()

import matplotlib.pyplot as plt
import seaborn as sns

#% pylab inline
ax = age_no_nan_grouped.plot.area(colormap= 'jet', fontsize=12)

ax.set_title('Sibling number aboard the Titanic and survival', fontsize=15)
ax.set_xlabel('Survived or not, how many siblings, age', fontsize=15)
ax.set_ylabel('Passenger number', fontsize=15)

