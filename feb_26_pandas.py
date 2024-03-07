import pandas as pd
data=[10,20,30]
my_series=pd.Series(data)
print(my_series)

#for indedxing
a=["x","y","z"]
my_series2=pd.Series(data,index=a)
print(my_series2)

#data2=dict(name=["tr","us","ha"],age=[60,56,57],city=["surat","baroda","ahm"])
#this gives key value in alphabetical value
data2={'name':["tr","us","ha"],'age':[60,56,57],'city':["surat","baroda","ahm"]}
my_dataframe=pd.DataFrame(data2,columns=["NAME","AGE","CITY"])
print(my_dataframe)

#creating dataframe using 2d list

data3=[["tr",60,'surat'],["us",56,'baroda'],["ha",78,"ahm"]]
my_dataframe2=pd.DataFrame(data3,columns=["NAME","AGE","CITY"])
print(my_dataframe2)

data4=[["tr","us","ha"],[60,56,57],["surat","baroda","ahm"]]
my_dataframe3=pd.DataFrame(data4,index=["NAME","AGE","CITY"])
print(my_dataframe3)

#setting name column as index
#setting our variable as index

df=pd.DataFrame(data2)
df.set_index("name",inplace=True)
print(df)

#giving range to index

df2=pd.DataFrame(data2,index=pd.RangeIndex(5,8,name="serial no"))
print(df2)

df3=pd.DataFrame(data2)
print(df3)
print("index:",df3.index)
print(df3.index.values)

df3.rename(index={0:"a",1:"b",2:"c"},inplace=True)
print(df3)

