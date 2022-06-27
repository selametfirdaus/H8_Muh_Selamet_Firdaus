# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:49:29 2022

@author: 089582
"""

import numpy as np

a = np.array([1, 2, 3])


np.zeros(6)

np.ones(6)

np.empty(6)


########

print(np.arange(4))
print(np.arange(0,10,2)) # (start, stop, step)

print(np.arange(10))
print(np.arange(0,20,2)) # (start, stop, step)

#######

np.arange(2,29,5)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])


###########
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example)

array_example.ndim
array_example.size

##########

a = np.arange(6)

print(a)

######
b = a.reshape(3,2)

print(b)

b = a.reshape(3,1)

print(b)












