#day1 import pandas and convert list to dataframe
import pandas as pd
list=[12,34,56,78,90,23,45]
s=pd.Series(list)
print(s)
df=pd.DataFrame(s,columns=['values'])
print(df)
#day2 multi_dimentional list and dictenary to pandas
list1=[['Kolkata','Delhi','Kerola','Mumbai','Chenni'],['Gujrat','Bengaluru','Hydrabad','Kerala','Taminadu']]
df=pd.DataFrame(list1,columns=['City1','City2','City3','City4','City5'])
print(df)
dict={'Name':['akash','rohit','manaj'],
      'Age':[24,26,28],
      'City':['kolkat','kerola','Mumbai']}
dict_dataframe=pd.DataFrame(dict)
print(dict_dataframe)
#day3 set and tuple to pandas
set={1,2,3,4,5,6,7,8,9}
df1=pd.DataFrame(set,columns=['Set_value'])
print(df1)
tup1=(12,89,56,42,21,47)
df=pd.DataFrame(tup1,columns=['Tuple_value'])
print(df)
#day4 datatype in pandas numeric datatype
dict1={'Age':[25,30,23,38,29],
       'Salary':[24000,41000,38000,21111,23332]}
numeric_datatype=pd.DataFrame(dict1)
print(numeric_datatype)
print(numeric_datatype.info())
print(numeric_datatype.dtypes)
numeric_datatype['Age']=numeric_datatype['Age'].astype('int8')
numeric_datatype['Salary']=numeric_datatype['Salary'].astype('int32')
print(numeric_datatype.info())
#date5 datetime
date={'Name':['Akash','Bijoy','Majnu'],
     'Age':[25,28,78],
     'Job_role':['software engineer','data science','Teacher'],
     'Salary':[60000,50000,45000]}
print(date)
date_dataframe=pd.DataFrame(date)
print(date_dataframe)
print(date_dataframe.dtypes)
dates=['2024-10-04','2023-11-15','20218-10-23']
datetime={'date':dates}
date_dataframe=pd.DataFrame(datetime)
print(date_dataframe)
print(date_dataframe.dtypes)
# Sample dataframe with a datetime column
df = pd.DataFrame({'datetime_column': ['2024-02-10 08:30:00', '2024-02-11 09:45:00']})
# Convert datetime column to date
df['date_column'] = pd.to_datetime(df['datetime_column']).dt.date
print(df)
#how to read csv file using pandas
csv_read=pd.read_csv('age.csv')
cs_read=pd.read_csv('age.csv')
print(cs_read)

first_five_row=csv_read['income'].head()
print(first_five_row)
#excel=pb.read_excel('age.xlsx')
#print(excel)
row ,col=csv_read.shape
print("No of row:",row)
print("No of column",col)
# show first five row
print("First 5 row")
print(csv_read.head())
# show first three row
print("First 5 row")
print(csv_read.head(3))
# show last five row
print("last five row")
print(csv_read.tail())
# show last three row
print("last three row")
print(csv_read.tail(3))
# shows specific row within range
print("show 4 to 7")
print(csv_read[4:8])
#column acccess
print(csv_read.columns)
#show specific colmn
print(csv_read['age'])
print(csv_read[['age','income']])
print(csv_read[['age','income']].head())
#statical calculation using pandas
max_age=csv_read['age'].max()
print("oldest person in our group ",max_age)
max_sal=csv_read['income'].max()
print("Your maximum salary is=",max_sal)
avg_salary=csv_read['income'].mean()
print("Average_salary",avg_salary)
std_salary=csv_read['income'].std()
print("Stadard_davition slary",std_salary)
print(csv_read.columns)
# mode most frequency number
mod_salary=csv_read['income'].mode()
print("Stadard_davition slary",mod_salary)
# 95% of salary
per_salary=csv_read['income'].quantile(0.95)
print(" 95% salary",per_salary)
#Sorting method 
sort_acc_salary=csv_read['income'].sort_values()
print("Salary in accending order",sort_acc_salary)

sort_acc_salary=csv_read['income'].sort_values(ascending=False)
print("Salary in discending order",sort_acc_salary)
#conditional statment in pandas
print(csv_read['income']>35000)
df1=csv_read[csv_read['income']>35000]
print("salary grater the 35000")
print(df1)
df2=csv_read[(csv_read['income']>35000) | (csv_read['age']>30)]
print(df2)

df3=csv_read[(csv_read['income']>35000) & (csv_read['age']>30)]
print(df2)
#conditional using isin() function
df4=csv_read[csv_read['age'].isin([20,21,22,25,30,35])]
print(df4)
#shows record of those employee who work in kolkata and age gratter then 25
df5=csv_read[(csv_read['office']=='kolkata') & (csv_read['age']>30)]
print(df5)
# shows the record of those employee who work in kolkata or delhi and job role is engineer and #getting salary grater then 30000 and job role eaither engineer or teacher or nurse,
df6=csv_read[(csv_read['office'].isin(['kolkata','delhi'])) & (csv_read['job_role'].isin(['engineer','teacher','doctor','nurse'])) &
             (csv_read['income']>30000)]
print(df6)
#how to delete a column in your dataframe
del csv_read['Language']
print(csv_read)
#how to delete row in your dataframe
df7=csv_read.drop([0,1])
print("After drop 1st and 2nd row")
print(df7)
#how to rename and concat column name
dict1={
  'Name':['Akash','Bijoy','Pijush'],
  'Age':[25,23,28]
}
dict2={
  'name':['Ayush','Nayan','Sapna'],
  'age':[38,28,35]
}
dataf1=pd.DataFrame(dict1)
dataf2=pd.DataFrame(dict2)
print(dataf1)
print(dataf2)
dataf1=dataf1.rename(columns={'Name':'name','Age':'age'})
print(dataf1)
concat_two_df=pd.concat([dataf1,dataf2],axis=1)
print(concat_two_df)