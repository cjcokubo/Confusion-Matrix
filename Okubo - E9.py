# Author: Christine Okubo
# Date: 12-13-20
# Input: 1) x-base, 2) null dist., 3) signal dist., 4) threshold value
# Output: a 2x2 confusion matrix

def confusionMatrix (x, y0, y1, threshold):
    import numpy as np
    x_array = np.array(x)
    y0_array = np.array(y0)
    y1_array = np.array(y1)
    
    i = np.where(x_array == threshold)[0][0]
    
    true_pos = np.sum(y1_array[i+1:])
    false_pos = np.sum(y0_array[i+1:])
    
    false_neg = np.sum(y1_array[0:i+1])
    true_neg = np.sum(y0_array[0:i+1])
    
    positives = np.append(true_pos, false_pos)
    negatives = np.append(false_neg, true_neg)
    
    confusion_matrix = np.concatenate(([positives], [negatives]), axis=0)
    return confusion_matrix