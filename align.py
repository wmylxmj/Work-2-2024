# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:16:43 2024

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt
import dtw

def dtw_align(seqref, seqin):
    manhattan_distance = lambda x, y: np.abs(x - y)
    d, cost_matrix, acc_cost_matrix, path = dtw.dtw(seqref, seqin, dist=manhattan_distance)
    indices = []
    for i in range(len(path[1])):
        index = path[1][i]
        if len(indices) - 1 < index:
            indices.append(path[0][i])
            pass
        else:
            if abs(seqin[index]-seqref[path[0][i]]) < abs(seqin[index]-seqref[indices[index]]): 
                indices[index] = path[0][i]
                pass
            pass
        pass
    return np.array(indices)