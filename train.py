#titatnic

import pandas as pd
df=pd.read_csv("train.csv") 
#print(df.head(10))
#print(df.tail(10))
#print(df.describe())
#print(df[df["Age"]>30].describe())
print(df.sort_values(["Age","Name"],ascending=[True,False]).loc[:,["Name","Age"]])
