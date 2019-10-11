import pandas as pd

lst=["I","got","a","brand","new","pushbike"]

df=pd.DataFrame(lst,index=['a','b','c','d','e','f'],columns=["words"])
#print(df)

lst2=[11,12,13,14,56]
df2=pd.DataFrame([lst,lst2])
#print(df2)

df3=pd.DataFrame(list(zip(lst,lst2)),columns=["words","values"])
print(df3)
