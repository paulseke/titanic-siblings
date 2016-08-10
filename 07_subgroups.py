# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:29:12 2016

@author: seke
"""

# Returns the age of people with a given number of siblings, who survived
def age_data_parser_survivors (low, high, df):
    prser = df[(df['Survived'] > 0) & (df['SibSp'] > low) & (df['SibSp'] < high)]
    return prser.reset_index(drop=True)

# Returns the age of people with a given number of siblings, who died
def age_data_parser_dead (low, high, df):
    prser = df[(df['Survived'] == 0) & (df['SibSp'] > low) & (df['SibSp'] < high)]
    return prser.reset_index(drop=True)
               
# Siblings: 0
df = age_no_nan_survived
low = -1
high = 1
age_survived_0 = age_data_parser_survivors (low, high, df)

df = age_no_nan_died
age_died_0 = age_data_parser_dead (low, high, df)

print age_survived_0['Age'].describe()
print ''
print age_died_0['Age'].describe()
print ''

# Siblings: 1
df = age_no_nan_survived
low = 0
high = 2
age_survived_1 = age_data_parser_survivors (low, high, df)

df = age_no_nan_died
age_died_1 = age_data_parser_dead (low, high, df)

print age_survived_1['Age'].describe()
print ''
print age_died_1['Age'].describe()
print ''

# Siblings: 2+
df = age_no_nan_survived
low = 1
high = (age_df_no_nan['SibSp'].max())+1
age_survived_2 = age_data_parser_survivors (low, high, df)

df = age_no_nan_died
age_died_2 = age_data_parser_dead (low, high, df)

print age_survived_2['Age'].describe()
print ''
print age_died_2['Age'].describe()
print ''

# Building the survival, in function of average age and number of siblings

survival_siblings_age_df = pd.DataFrame(
    data=[[(age_survived_0['Age'].mean()), (age_died_0['Age'].mean())],
          [(age_survived_1['Age'].mean()), (age_died_1['Age'].mean())],
          [(age_survived_2['Age'].mean()), (age_died_2['Age'].mean())]],
    index=['0','1','>2'],
    columns=['Survivors','Dead']
)


# Plotting the survivors and dead passengers age in function of sibling number
import matplotlib.pyplot as plt
import seaborn as sns

#% pylab inline

ax = survival_siblings_age_df.plot.bar(colormap='jet', fontsize=15)

ax.set_title('Sibling number aboard the Titanic, age and survival', fontsize=15)
ax.set_xlabel('Number of siblings', fontsize=15)
ax.set_ylabel('Passenger age', fontsize=15)
ax.set_ylim([0,50])
#legend(labelspacing=0.25, fontsize = 15)

