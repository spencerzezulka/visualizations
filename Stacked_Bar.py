import matplotlib.pyplot as plt
import numpy as np

def stacked_bar(x_arr, y_arr, ax, colors, labels, hbar=True, **kwargs):
    '''
    this function takes in two np arrays and creates a stacked bar plot where the edge of each bar represents the
    corresponding value, as well as a dictionary mapping the scenario/system/element variables to colors, and another
    dictionary to map said variables to labels.
    
    x_arr: 1-dimensional np array of shape (n, ), where n is the number of categorical variables (scenarios)
    y_arr: 2-dimensional np array of shape (m, n), where m is the number of subsystems, systems, or elements
    colors: dictionary mapping the indices of y_r to matplotlib color values
    ax: matplotlib.axes object on which to plot the stacked bar
    hbar: bool, determines if plots are horizontal or vertical


    '''
    for i, x in enumerate(x_arr):
        sorted_y_arr = sorted(y_arr[:, i], reverse=True)
        sorted_y_arr_pos = [index for index, num in sorted(enumerate(y_arr[:, i]), key=lambda x: x[-1], reverse=True)]
        for j, y in enumerate(sorted_y_arr):
            if hbar:
                if i==(len(x_arr)-1):
                    ax.barh(x, y, color=colors[sorted_y_arr_pos[j]], label=labels[sorted_y_arr_pos[j]], **kwargs)
                else:
                    ax.barh(x, y, color=colors[sorted_y_arr_pos[j]], **kwargs)
            else:
                if i==(len(x_arr)-1):
                    ax.bar(x, y, color=colors[sorted_y_arr_pos[j]], label=labels[sorted_y_arr_pos[j]], **kwargs)
                else:
                    ax.bar(x, y, color=colors[sorted_y_arr_pos[j]], **kwargs)
    return ax