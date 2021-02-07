#Module Name : lec04_lambda.py
import pandas as pd
import numpy as np

def add(x):
    res = 10 + x
    return res

res =add(7)
print(res)
#-------------------------------------------
변수 = lambda x: x + 10
res = 변수(6)
print(res)

df = pd.read_csv("emp.csv", index_col="empno")
# df.apply(람다식)
# df.map(람다식)
# df.applymap(람다식)
# --------------------------------------------------------
# update emp set deptno="십십" where deptno=10
# df["deptno"] = df["deptno"].apply(lambda x : "십십" if (x ==10)   else x )
# print("-------done------")
# print(df.head(10))
# --------------------------------------------------------
def deptnoCheck(DEPTNO):
    str = ""
    #if df["deptno"] == 10:
    if DEPTNO == 10:
        str = "aaa"
    else :
        str = "bbb"
    return str

df["dummy"] = df["deptno"].apply(lambda x : deptnoCheck(x))
print("-------done------")
print(df.head(10))
# --------------------------------------------------------

data =   {
        "uid":['kim','lee','park','hong'],
        "upw":['11','22','33','44'],
        "uname":['김','리','박','홍'],
        "addr":['서울','경기','서울','인천']
        }

pd = pd.DataFrame(data=data)
print(pd.head())
#1. 데이터프레임화

#2. 람다식사용 : 서울인 경우:02  인천:032  경기:031   --> "lcode" 컬럼에 적용

#3. 람다식+함수 사용 : 서울인 경우:02  인천:032  경기:031   --> "lcode" 컬럼에 적용



myFrame["lcode"] = df["addr"].apply(lambda x : myCheck(x))
print(myFrame)


# #by 정진우
# def myCheck(ADDR) :  #df["addr"]
#     str = ""
#     if ADDR == "서울":
#         str = "02"
#     elif ADDR =="인천":
#         str = "032"
#     elif ADDR =="경기":
#          str = "031"
#     return str
#
# myFrame["lcode"] = df["addr"].apply(lambda x : myCheck(x))
# print(myFrame)
#
# #by 정진우
# myFrame["lcode"] = myFrame["addr"].apply(lambda x :
#
# "02" if (x=="서울")
#      else
#         ("032" if (x=="인천")
#                else
#                     ("031" if (x=="경기") else x )
#         )
# )
# print(myFrame)
#
#
# myFrame["lcode"] = myFrame["addr"].apply(lambda x :
#                             "02" if (x=="서울")
#                                  else
#                                     "032" if (x=="인천")
#                                           else "031")   #if (x=="경기") else x)
# print(myFrame)
#
# #정진우
# myFrame["lcode"] = myFrame["addr"].apply(lambda x : "02" if (x=="서울")
#                                else "032" if (x=="인천")
#                                else "031" if (x=="경기"))
# print(myFrame)



#by 박정원
df2 = pd.DataFrame(data)
print(df2)

def lcodeFun(ADDR):  #df2["addr"]
    lc = ""
    if ADDR == '서울':
        lc = "02"
    elif ADDR == '인천':
        lc = "032"
    elif ADDR == '경기':
        lc = "031"
    return lc

df2["lcode"] = df2["addr"].apply(lambda x: lcodeFun(x))
print(df2)

df2["addr"].apply(lambda x:"02" if(x == "서울") else("031" if(x == "경기") else("032")))
#"02" if(x == "서울") else("031" if(x == "경기") else("032"))
df2["lcode2"] = df2["addr"].apply(lambda x:
                                  "02" if(x == "서울")
                                       else(
                                            "031" if(x == "경기")
                                                  else("032")
                                           )
                                  )
print(df2)

#by 유연재
data = { "uid":['kim','lee','park','hong'],
         "upw":['11','22','33','44'],
         "uname":['김','리','박','홍'],
         "addr":['서울','경기','서울','인천']
       }

#1. 데이터 프레임화
df1 = pd.DataFrame(data = data)
print(df1)

#2. [람다식 사용] : 서울인 경우: 02, 인천인 경우: 032, 경기: 031 / "locde" 컬럼에 적용
df1['locde'] = df1['addr'].apply(lambda x: "02" if x == '서울' else "032" if x == '인천' else '031')
#람다식은 elif 사용 불가능
print(df1)

#3. [람다식+함수 사용] : 서울인 경우: 02, 인천인 경우: 032, 경기: 031 / "locde" 컬럼에 적용
def lonum(x):
    num = 0
    if x == '서울':
        num = '02'
    elif x == '인천':
        num = '032'
    else:
        num = '031'
    return num

df1['locde'] = df1['addr'].apply(lambda x: lonum(x))
print(df1)

