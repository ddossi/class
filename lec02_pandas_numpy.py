# module name : lec02_pandas_numpy.py
import numpy as np
# 1. array ndtype      1 2 3
# 2. List             [1,2,3,]
# 3. Series    Series([1,2,3,])
vlist = [1,2,3]
print(vlist)

vlist = [[1,2,3],
         [1,2,3]
         ]
print(len(vlist), len(vlist[0]))


varr = np.array(vlist)
print(varr)

vmatrix = [ [1,2,3] , ['a','b','c'] ]
varr2 = np.array(vmatrix)
print(varr2)
print(varr2.shape)
print(varr2[1][2])

# list[] tupl() dict{}
# tupl = (1,2,3)
# set = (1,1,1,2,3)  #123  select distinct deptno from emp

dict = [{"id":"kim" , "pw":"111"} ,
        {"id":"park" , "pw":"222"}
        ]
print(type(dict))
print(dict[0]["pw"])

dict = {"record1" : {"id":"kim" , "pw":"111"} ,
        "record2" : {"id":"park" , "pw":"222"}
        }
print(type(dict))
print(dict["record2"]["pw"])




import pandas as pd
s = pd.Series(["a",'b','c','d'])
print(s.shape)    # (4,  )  (행 , )
print(s)
print(s.dtype)   #int64   float64  object

#def __init__(self,
# data=None,
# index=None,
# columns=None,
# dtype=None,
# copy=False):
#data : dict np list series
list = [[7733,'kim','111'],[8855,'lee','222']]
df = pd.DataFrame(data=list,
                  columns=['eno','id','pw'] )
print(df)
print(df.shape)
print(df.head())
print(df.tail(10))










