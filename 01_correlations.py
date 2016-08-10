# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:09:10 2016

@author: seke
"""

# Total number of passengers who survived or died
print titanic_df.groupby('Survived')['PassengerId'].count()
print ""

# Count of passengers who survived and died grouped according to their number of siblings aboard
D = titanic_df.groupby(['Survived','SibSp'], as_index=False)['PassengerId'].count()
print D

# Creating a DataFrame including information on the survival of the proportion of people with siblings

dead_numpy_array = np.array(D['PassengerId'][0:7]) # remove the index
dead_pd_series = pd.Series(dead_numpy_array, index = ['0','1','2','3','4','5','6']) # attribute the index    
              
survivors_numpy_array = np.array(D['PassengerId'][7:12]) # removes the index from survivors
survivors_numpy_array = np.append(survivors_numpy_array,[0,0]) # add the value zero to get same size as the dead (7)
survivors_pd_series = pd.Series(survivors_numpy_array, index = ['0','1','2','3','4','5','6']) # attribute the same index as the dead            

siblings_number_df = pd.concat([dead_pd_series, survivors_pd_series], axis=1)
siblings_number_df.columns = ['died', 'survived']

siblings_proportion_df = siblings_number_df.div(siblings_number_df.sum())
print 100*siblings_proportion_df

# Plotting the Dataframe for preliminary observations and data-based hypotheses
import matplotlib.pyplot as plt
import seaborn as sns

# plotting the dataframe
#% pylab inline
ax =(100*siblings_proportion_df).plot(lw=2,colormap='jet',marker='.',markersize=15, fontsize=12)

ax.set_title('Sibling number aboard the Titanic and survival', fontsize=15)
ax.set_xlabel('Number of siblings aboard', fontsize=15)
ax.set_ylabel('People with siblings aboard (%)', fontsize=15)
#legend(labelspacing=0.25, fontsize = 15)


