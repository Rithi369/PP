import pandas as pd

data1 = {
    'RollNo':[1,2,3],
    'Name':['Amogh','Babitha','Chaitanya'],
    'TotalMarks':[95,88,96]
}
data2 = {
    'RollNo':[4,5,6],
    'Name':['David','Eshan','Ganesh'],
    'TotalMarks':[82,91,70]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("Original DataFrames : ")
print()
print(df1)
print("-"*50)
print(df2)
print("-"*50)
print("After joining the said two dataframes along rows : ")
print("-"*50)
result_df = pd.concat([df1,df2], ignore_index = True)
print(result_df)