# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 02:24:50 2016

@author: seke
"""

# Plotting age distribution of passengers who died or survived

# Formatting variables for plotting
a = age_no_nan_died['Age']
b = age_no_nan_survived['Age']
c = pd.concat([age_no_nan_died['Age'], age_no_nan_survived['Age']], axis=1)
d = np.array(c)
n_bins = 10

fig, axes = plt.subplots(nrows=1, ncols=3, sharex=True , sharey=True)
ax0, ax1, ax2 = axes.flat

ax0.hist(a, n_bins, normed=0, histtype='bar')
ax0.set_title('Age-dead', fontsize=15)
ax0.set_fontsize=12
ax0.set_xlabel('------------------', fontsize=15)
ax0.set_ylabel('Frequency', fontsize=15)
ax0.set_ylim([0,120])
ax0.set_xlim([0,80])

ax1.hist(b, n_bins, normed=0, histtype='bar')
ax1.set_title('Age-survivors', fontsize=15)
ax1.set_fontsize=12
ax1.set_xlabel('Age of passengers', fontsize=15)

colors = ['lime', 'blue']
ax2.hist(d, n_bins, normed=0, histtype='bar', color=colors, label=['Dead','Not'], stacked=False)
ax2.legend(prop={'size': 10})
ax2.set_title('Dead vs. survivors', fontsize=15)
ax2.set_xlabel('------------------', fontsize=15)
ax2.set_fontsize=12

fig.subplots_adjust(hspace=0.7)

