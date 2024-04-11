# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:23:22 2024

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt

def average_step(x, scale, offset):
    N = len(x)
    end = offset + scale * ((N - offset) // scale)
    x_cut = x[offset:end]
    x_scale = [x_cut[i::scale] for i in range(scale)]
    x_scale = np.sum(np.array(x_scale), axis=0)
    x_cut_new = np.zeros((len(x_cut)))
    for i in range(scale):
        x_cut_new[i::scale] = x_scale / scale
        pass
    x[offset:end] = x_cut_new
    return x

def average(x, scale, iteration):
    x_avg = x.copy()
    for i in range(iteration):
        for offset in range(scale):
            x_avg = average_step(x_avg, scale, offset)
            pass
        pass
    return x_avg