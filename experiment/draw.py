"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 3

means_men = (20, 35, 30)
std_men = (2, 3, 4)



fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Men')



plt.xlabel('')
plt.ylabel('Time error')
plt.title('')
plt.xticks(index + bar_width, ('Arduino', 'edison ',
		 'edison and arduino'))
plt.legend()

plt.tight_layout()
plt.show()