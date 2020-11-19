# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:24:28 2020

@author: Simon
"""

#Nov 16 Homework plot
import numpy as np
import matplotlib.pyplot as plt

data = np.array([22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 30, 20, 5, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27])

print(np.sort(data))
print(np.sum(data))
print(np.median(data))
#box
fig1, ax = plt.subplots(1, 2)
ax[0].set_title('box plot')
ax[0].boxplot(data)

#dot
unique, counts = np.unique(data, return_counts=True)
ax[1].set_title('dot plot')
ax[1].bar(unique, counts)


plt.show()