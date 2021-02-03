#Module name : lec03_emp_pandas.py
import numpy as np
import pandas as pd

df = pd.read_csv("emp.csv", index_col="empno")
print(df.info())
print(df.shape)
print(df.head())

# select ename from emp
print(df.ename)
print(df["ename"])
# select ename, sal from emp
print(df[["ename","sal"]])

# select empno||ename from emp;
# print(df["empno"] + df["ename"]) #error
print(df["job"] + df["ename"])

#select sal, sal*10 from emp;
print(df["sal"], df["sal"]*10)


list = [1,2,3,4,5]
dd = pd.DataFrame(data=list, columns=["no"])
print(dd.head())

list = [1,2,3,4,5]
arr = np.array(list)
dd = pd.DataFrame(data=arr, columns=["no"])
print(dd.head())


dic = {"uid":["kim","lee","park"]  ,
       "upw":["11","22","33"]  ,
       }
ser = pd.Series(["aa","bb","cc"])
dd = pd.DataFrame(data=dic)
dd["uname"] = ser
# dd["uname"] = (s for s in ser)
print(dd)
#    uid  upw  uname
# 0  kim  11   aa
# 1  lee  22   bb
# 2  park 33   cc

# select sal, ename from emp where deptno=10
print(df[["sal","ename"]]  [ df["deptno"]==10 ])
print( df[ df["deptno"]==10 ][["sal","ename"]] )

# df.ename df["ename"]
print( df[ df["deptno"]==10 ][["sal"]] )
print( df[ df["deptno"]==10 ]["sal"] )
print( df[ df["deptno"]==10 ].sal)


# select sal, ename from emp
# order by ename asc / desc
dd = df.sort_values(by="ename")
dd = df[["sal","ename"]].sort_values(by="ename", ascending=False)
print(dd)


# select sal, ename from emp where deptno=10
# order by ename asc
print(df[["sal","ename"]][df["deptno"]==10].sort_values(by="ename", ascending=False))
print( df[df["deptno"]==10][["sal","ename"]].sort_values(by="ename", ascending=False) )

dd["SC"] = df["sal"] + df["comm"]
print(dd)


# null   NaN np.non    is null
#select ename, comm from emp where comm is  null;
print(df[["ename","comm"]][df["comm"].isnull()])
print(df[df["comm"].isnull()==False][["ename","comm"]])
# print(df[df[["ename","comm"]].isnull() == True]) #<----
# print(df[["ename","comm"]][df["comm"] == np.nan]  )
# print(df[df["comm"] == np.nan][["ename","comm"]]  )

# select count(1) from emp where comm is null;
# order by  --> sort_values()
# count(1)  --> value_counts()
print( df["ename"][df["comm"].isnull()])

# Group 함수 :
# count(1) --> value_counts()
# avg      --> mean()
# max      --> max()
# min      --> min()
# sum      --> sum()
# group by --> groupby()

# select deptno, avg(sal) from emp
# group by deptno
# --order by deptno;
print( df.groupby(by="deptno", sort=True)["sal"].mean() )

# select deptno, min(sal), max(sal)
# from emp
# group by deptno;
# print( df.groupby(by="deptno") [["sal"].min() , ["sal"].max()])
# dic = {"sal":"max", "sal":"min"}
# print( df.groupby(by="deptno").agg(dic))
print( df.groupby(by="deptno")["sal"].agg([max, min])   )

# delete from emp where ename='SMITH'
# delete  --> drop()

# [가로]레코드삭제   : axis = 0, index = 7499               inplace = False
# [세로]job컬럼 삭제 : axis = 1, columns = ['job','mgrno'], inplace = False

#delete from emp where empno=7499;
# =================drop test 후 주석처리 했음
# dfcp = df.drop(index=[7499])
# print(dfcp)
# df.drop(axis=0, index=[7499], inplace = True)
# print(df)
#
# df.drop(axis=1, columns=["job","mgrno"], inplace=True)
# print(df)

# print(df.columns)
#delete from emp where ename='SMITH';
idx = df[df["ename"]=='SMITH'].index  #[]
#df.reset_index("ENAME")
print(idx)
df.drop(index=idx, axis=0, inplace=True)
# df.drop(index=[7499])
print(df)

#### np.non --> NaN  (결측치 데이터 제거*****************)
dfcp = df
#dfcp = dfcp.dropna()
dfcp.dropna(inplace=True)
print(dfcp)

dfcp = df
print(dfcp.isnull().sum())

# slicing  : iloc[인덱스] loc[값]   --> XXXXXXX ixloc[]

# iloc[행, 렬]	iloc[2,4]
# iloc[s:e , s:e]	iloc[0:3 , 0:2]
# 슬라이싱 ::::: s<=I<e   -1(맨끝 칸/줄)
# loc[인덱스값, 컬럼명]
# loc[ [,,,] , s:e]

#8개 값을 2덩어리  --> 1덩어리에 4개씩
list = [[1,2,3,4],
        [5,6,7,8]
       ]
print(len(list),  len(list[0]))
arr = np.array(list)
print(arr.shape)

#8개 값을 4덩어리  --> 1덩어리에 2개씩
arr = arr.reshape(4,-1)  #-1은 자동계산된 어떠한 값을 의미
print(arr.shape)
print(arr)

#8개 값을 ?덩어리  --> 1덩어리에 4개씩
arr = arr.reshape(-1,8)  #-1은 자동계산된 어떠한 값을 의미
print(arr.shape)
print(arr)

#--------------------------- insert
# insert into emp values(9999,'MYNAME','JJJ','','','','','')
list = ['MYNAME','JJJ','','','','','']
#col = ['ename', 'job', 'mgrno', 'hiredate', 'sal', 'comm', 'deptno']
col = df.columns
#idx = df.index
#--------------------------------
# 기존 list 데이터를 Dataframe[신규]으로 만들고 합쳐야 하는 불편함
# Dataframe[기존] + Dataframe[신규]
insdf = pd.DataFrame(data=[list], columns=col)
print(insdf)
df = df.append(insdf)  #, ignore_index=True)
# df = df.reset_index()
print(df)

# list = ['MYNAME','JJJ','','','','','']
dic = {"ename":"DICNAME", "job":"JJJ"}
df = df.append(dic, ignore_index=True)
print(df)

df.loc["9898"] = ['MYNAME','JJJ','','','','','']
print(df)


#--------------------------- update
#--------------------------- lambda update,
#--------------------------- map apply      applymap ....
def add(x) :
       res = 10 + x
       return res
print(add(7))

mylam = lambda x : x + 10
print(mylam(6))

#---- 선형대수 : 행렬
#-----행렬변환------------------- .T  전치(Transpose):비벗화
# stack v. h _c _r



