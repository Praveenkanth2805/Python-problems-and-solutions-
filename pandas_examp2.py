import pandas as pd
from sklearn.linear_model import LinearRegression

ass=int(input("assignment given(1-5):"))
att=int(input("attedence percentage:"))
cia=int(input("cia mark(12-25):"))
behave=input("behavior (good,average,not good,worst):")

if ass == 1 :
    ass = 12
elif ass==2:
    ass = 14
elif ass==3:
    ass = 18
elif ass==4:
    ass = 22
else:
    ass = 24

if behave=='good':
    behave=25
elif behave=='average':
    behave=20
elif behave=='not good':
    behave=18
else:
    behave=12

data = {
    'assignment':[ass], 'attedence':[att], 'cia_test': [cia], 'behavior':[behave]
    }

df=pd.DataFrame(data)
df['attedence']=(df['attedence']/100)*25
df['Internal_mark']=(df['assignment']+df['attedence']+df['cia_test']+df['behavior'])/4
df['Internal_mark']=df['Internal_mark'].round()
print(df)
