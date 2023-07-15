import numpy as np
def solution(nums):
    if int(len(nums)/2) < len(np.unique(nums)):
        return int(len(nums)/2)
    else:
        return len(np.unique(nums))