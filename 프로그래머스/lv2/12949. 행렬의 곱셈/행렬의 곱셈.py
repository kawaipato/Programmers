import numpy as np
def solution(arr1, arr2):
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    nam = a1.dot(a2)
    return nam.tolist()
        