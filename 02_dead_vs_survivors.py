# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:13:41 2016

@author: seke
"""

# Creating a DataFrame including information on the survival of the proportion of people with siblings

dead_numpy_array_2_groups = np.array(D['PassengerId'][0:2]) # remove the index from the dead
dead_numpy_array_1_group = (D['PassengerId'][2:6]).sum() # summing up passenger numbers with more than 2 siblings on board
dead_numpy_array_3_groups = np.append(dead_numpy_array_2_groups, dead_numpy_array_1_group)
dead_pd_series_3_groups = pd.Series(dead_numpy_array_3_groups) # attribute the index    
              
survivors_numpy_array_2_groups = np.array(D['PassengerId'][7:9]) # removes the index from survivors
survivors_numpy_array_1_group = (D['PassengerId'][9:12]).sum() # summing up passenger numbers with more than 2 siblings
survivors_numpy_array_3_groups = np.append(survivors_numpy_array_2_groups, survivors_numpy_array_1_group)
survivors_pd_series_3_groups = pd.Series(survivors_numpy_array_3_groups)            

siblings_number_df_3_groups = pd.concat([dead_pd_series_3_groups, survivors_pd_series_3_groups], axis=1)
siblings_number_df_3_groups.columns = ['died', 'survived']

siblings_percent_df = 100*siblings_number_df_3_groups.div(siblings_number_df.sum())

print siblings_percent_df

# Plotting the Dataframe for preliminary observations and data-based hypotheses
import matplotlib.pyplot as plt
import seaborn as sns

#% pylab inline
ax =(siblings_percent_df).plot.bar(colormap= 'jet', fontsize=12)

ax.set_title('Sibling number aboard the Titanic and survival', fontsize=15)
ax.set_xlabel('Number of siblings aboard', fontsize=15)
ax.set_ylabel('People with siblings aboard (%)', fontsize=15)
#legend(labelspacing=0.25, fontsize = 15)
