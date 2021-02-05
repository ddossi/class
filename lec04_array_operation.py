#Module name : lec04_array_operation.py
import numpy as np
a = [1,2,3]
b = [4,5,6]
c = np.array(a)
d = np.array(b)

matrix = [[1,2,3],[4,5,6]]
print(np.array(matrix))
print(np.array(matrix).T)  #<--********
print(np.array(matrix).transpose())


# 세로줄 합치기
# [1,   4
# 2,  + 5
# 3,    6]
# print(np.c_[a,b])
# print(np.column_stack([a,b]))
# print(np.concatenate((c.T, d.T), axis=1))


# 위아래로 합치기  [1,2,3]
#                [4,5,6]
# print(np.r_[[a],[b]])
# print(np.vstack([a,b]))
# print(np.concatenate((c,d), axis=0) )

# 옆으로 합치기  [1,2,3] + [4,5,6]
# print(np.r_[a,b])                       #[1 2 3 4 5 6]
# print(np.hstack([a,b]))                 #[1 2 3 4 5 6]
# print(np.concatenate((c,d), axis=0) )   #[1 2 3 4 5 6]
# print(np.array(a+b))                    #[1 2 3 4 5 6]
# print("리스트:",a+b)                              #[1, 2, 3, 4, 5, 6]

