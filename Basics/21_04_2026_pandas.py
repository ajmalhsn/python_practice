import pandas as pd

# Example-1 (1D)
# data = [10,20,30,40,50]
# dataFrame = pd.Series(data)
# print(dataFrame) # dataFrame is created based on the array data

# Example -2 (2D)

data = {
    "name": ["Std1","Std2","Std3","Std4","Std5","Std6","Std7","Std8"],
    "marks": [10,20,30,40,50,60,70,80]
}

df = pd.DataFrame(data)
print(df)
print(df.head()) # first 5 rows
print(df.head(7)) # first 7 rows

print(df.tail()) # last 5 rows
print(df.tail(6)) # last 6 rows

print(df.sample()) # randomly will fetch 1 record 
print(df.sample(8)) # randomly fetch 8 records

print(df.sample(frac=0.5)) # 50% of the records

print(df.shape) # print row and columns of data frame
print(df.size) # number of elements of the data frame
print(df.ndim) # dimension of the data frame
print(df.columns) # name of all columns 
print(df.index) # index range
print(df.dtypes) # datatypes of rows 

print(df.info()) ## complete info of all columns and memory being used
print(df.describe()) ## first numerical columns with mathematical calculations
print(df.describe(include="all")) ## includes all numerical columns with mathematical calculations complete properties like min,max, sum, 25%, 50%, 75%, count

print(df.iloc[0]) ## give me row at 0th position
print(df.iloc[0]) ## based on label 

df.index = [100,200,300,400,500,600,700,800]
print(df.loc[100]) # will give row based on label
print(df.iloc[0]) # will give result only based on index

print(df.loc[0:2])
print(df.iloc[0:2])
print(df[(df["marks"] > 50) & (df["marks"] < 90)])

print(df.sort_values("marks"))
print(df.sort_values("marks",ascending=False))
print(df.sort_index())

excel_df = pd.read_csv("employees.csv")

print(excel_df[["Name","Age"]])
print(excel_df.isnull()) # null values
print(excel_df.notnull()) # not null values

print(excel_df.dropna()) ## drops null values
print(excel_df.dropna(axis=1))
print(excel_df.fillna(0))
print(excel_df.ffill())
print(excel_df.bfill())

print(excel_df["Age"].fillna(excel_df["Age"].mean()))

