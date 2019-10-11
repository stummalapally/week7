import pandas as pd

lst=["USA","France"]
df=pd.DataFrame(lst,columns=["Country"])
print(df[df["Country"]!='France'])