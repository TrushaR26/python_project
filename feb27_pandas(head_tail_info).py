import pandas as pd
data={'name':["john","alice","bob","emma","mike","sarah","david","linda","tom","emily"],
           "age":[25,30,35,28,32,27,40,33,27,31],
            "city" :["new york",'paris','london','sydney','tokyo','berlin','rome','madrid','toronto','moscow']}
print(data)
df=pd.DataFrame(data)
print(df)
#print("first three rows")
#print(df.head(3))
#print("first five rows by default")
#print(df.head())
##gives last 5 obs by default
#print(df.tail())
#gives information regarding the
#print(df.info())
#print(df.info(3))

#dataframe manipulation
#adding new column
#qualification=['bsc','bba','bca','bsc','bba','bca','bsc','bba','bca','msc']
#df['Qualification']=qualification
#print(df)
#add new row
#df.loc[len(df.index)]=['amy',33,'ahm','BIT']
#print("modified dataframe")
#print(df)
