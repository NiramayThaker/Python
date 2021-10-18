import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    min_of_arr = min(arr)
    max_of_arr = max(arr)
    
    try:
        max_sum = 0
        for i in arr:
            if i!=max_of_arr:
                max_sum += i 
        if max_sum != 0:
            print(max_sum)
        
        min_sum = 0
        for i in arr:
            if i!=min_of_arr:
                min_sum += i 
        if min_sum != 0:
            print(min_sum)
    finally:        
        min_ = 0
        count = 0

        for i in arr:
            count += 1
            if count <= len(arr)-1:
                min_ += i
                
        if max_sum > 0:
            return
        print(min_, end=' ')
        print(min_)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
