# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:34:27 2016

@author: seke
"""

import pandas as pd
import scipy.stats

# Assessing the statistical significance of diffences in age between survivors and dead with no sibling aboard
print '(survivor mean, standard deviation):', (age_survived_0['Age'].mean(), age_survived_0['Age'].std()) 
print ''
print '(dead passenger mean, standard deviation):', (age_died_0['Age'].mean(), age_died_0['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_0['Age'], age_died_0['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between survivors and dead with 1 sibling aboard

print '(survivor mean, standard deviation):', (age_survived_1['Age'].mean(), age_survived_1['Age'].std()) 
print ''
print '(dead passenger mean, standard deviation):', (age_died_1['Age'].mean(), age_died_1['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_1['Age'], age_died_1['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between survivors and dead with 2 or more siblings aboard

print '(survivor mean, standard deviation):', (age_survived_2['Age'].mean(), age_survived_2['Age'].std()) 
print ''
print '(dead passenger mean, standard deviation):', (age_died_2['Age'].mean(), age_died_2['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_2['Age'], age_died_2['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between survivors without and with one sibling aboard
print '(No siblings mean, standard deviation):', (age_survived_0['Age'].mean(), age_survived_0['Age'].std()) 
print ''
print '(One sibling passenger mean, standard deviation):', (age_survived_1['Age'].mean(), age_survived_1['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_0['Age'], age_survived_1['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between survivors without and with 2+ sibling aboard
print '(No siblings mean, standard deviation):', (age_survived_0['Age'].mean(), age_survived_0['Age'].std()) 
print ''
print '(Two sibling passenger mean, standard deviation):', (age_survived_2['Age'].mean(), age_survived_2['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_0['Age'], age_survived_2['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between survivors with only one againt 2+ sibling aboard
print '(One sibling mean, standard deviation):', (age_survived_1['Age'].mean(), age_survived_1['Age'].std()) 
print ''
print '(Two siblings passenger mean, standard deviation):', (age_survived_2['Age'].mean(), age_survived_2['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_survived_1['Age'], age_survived_2['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between dead without and with one sibling aboard
print '(No siblings mean, standard deviation):', (age_died_0['Age'].mean(), age_died_0['Age'].std()) 
print ''
print '(One sibling passenger mean, standard deviation):', (age_died_1['Age'].mean(), age_died_1['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_died_0['Age'], age_died_1['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between dead without and with 2+ sibling aboard
print '(No siblings mean, standard deviation):', (age_died_0['Age'].mean(), age_died_0['Age'].std()) 
print ''
print '(Two sibling passenger mean, standard deviation):', (age_died_2['Age'].mean(), age_died_2['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_died_0['Age'], age_died_2['Age'], axis=0, equal_var=False)
print ''

# Assessing the statistical significance of diffences in age between dead with only one againt 2+ sibling aboard
print '(One sibling mean, standard deviation):', (age_died_1['Age'].mean(), age_died_1['Age'].std()) 
print ''
print '(Two siblings passenger mean, standard deviation):', (age_died_2['Age'].mean(), age_died_2['Age'].std()) 
print ''
print 'Statistical analysis:', scipy.stats.ttest_ind(age_died_1['Age'], age_died_2['Age'], axis=0, equal_var=False)
print ''


