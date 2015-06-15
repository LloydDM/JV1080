'''
Created on Mar 1, 2015

@author: david
'''

#first = range(0.05, 5.0, 0.05)
#second = range(5.0, 7.0, 0.1)
#third = range(7.0, 10.5, 0.5)
# first = []
# second = []
# third = []
# fourth = []
# fifth = []

# i = 0
# while i < 4.9:
#     first.append(float("{:.2f}".format(i)))
#     i += 0.1
#  
#  
# i = 5
# while i < 10:
#     second.append(float("{:.2f}".format(i)))
#     i += 0.5


# i = 0
# while i < 10:
#     third.append(i)
#     i += 1
#       
# i = 10
# while i < 100:
#     fourth.append(i)
#     i += 10
#        
# i = 100
# while i < 1300:
#     fifth.append(i)
#     i += 100
#  
# final = []
# # final.extend(first)
# # final.extend(second)
# final.extend(third)
# final.extend(fourth)
# final.extend(fifth)
#  
# print tuple(final)
# print len(final)

# a = ["A" + str(100 - i) + ":" + str(i) + "B" for i in range(0, 101)]
# print tuple(a)

# a = range(0, 98, 2)
# b = range(100, 196, 4)
# c = range(200, 392, 8)
# d = range(400, 896, 16)

# # print a, b, c, d

# final = []
# final.extend(a)
# final.extend(b)
# final.extend(c)
# final.extend(d)

# print tuple(final)

import jvparams

print jvparams.PATCH_PITCH_PARAMS['P-ENV Velocity Sensitivity'].index(0)