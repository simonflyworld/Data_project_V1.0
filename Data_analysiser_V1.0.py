# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:33:45 2020

@author: Big DingDing
"""


import numpy as np
from scipy import stats
from scipy.stats import iqr

#data = np.array([45,51,55,64,66,68,70,71,71,71,73,76,82,83,84,90,95])
data = np.array([22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 30, 20, 5, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27])
def std(data):
    """
    STD function and Fuck Gallo

    Parameters
    ----------
    data : np.array
        The data

    Returns
    -------
    TYPE
        The STD of the data.

    """
    return np.std(data)


def zscore(data):
    """
    z score function and fuck Gallo
    
    Parameters
    ----------
    data : np.array
        The data

    Returns
    -------
    TYPE
        The z-score of the data.

    """
    return stats.zscore(data)

print("data : ", data)  
print("Q2 quantile of data : ", np.quantile(data, .50)) 
print("Q1 quantile of data : ", np.quantile(data, .25)) 
print("Q3 quantile of data : ", np.quantile(data, .75))  
#算SD
print("SD:",np.std(data))
#算zscore
print("Z-score:",stats.zscore(data))
#算mean
print("Mean(平均数)",np.mean(data))
#算median (中位数)
print("median（中位数）",np.median(data))
#算mode
print("Mode（高频数）",stats.mode(data))
#算range
print("range(范围)", max(data)-min(data))
#算IQR
print("IQR(Q3-Q1)(中间50%的范围)",iqr(data))
