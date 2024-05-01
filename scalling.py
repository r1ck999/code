#using python 
import pandas as pd 
def std_scalling(data):
  mean=data.mean()
  std=data.std()
  std_data=(data-mean)/std
  return std_data
data={
  'feature1':[10,20,30,40,50],
  'feature2':[11,12,13,14,15]
}
df=pd.DataFrame(data)
scaled_data_row=df.apply(std_scalling)
print(df)
print(scaled_data_row)
#using sklearn
import pandas as pd 
data={
  'feature1':[10,20,30,40,50],
  'feature2':[11,12,13,14,15]
}
df=pd.DataFrame(data)
print("Your original dataframe")
print(df)
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
std_data=scalar.fit_transform(df)
std_df=pd.DataFrame(std_data,columns=df.columns)
print("After Scalling your DataFrame")
print(std_df)



data1={'f1':[1,2,3,4],
      'f2':[4,5,6,7]}
print(data1)
df1=pd.DataFrame(data1)
print(df1)
l=[1,2,3,4,5]
print(l.mean())