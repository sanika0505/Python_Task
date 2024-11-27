import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('Data1.csv')

#display the first few rows of the data
print(df.head())

#Describe the data, get descriptive statistics for all numerical column
print(df.describe())

#find missing value in each column
mv = df.isnull().sum()
print("Missing value in each colume: \n", mv)

#calculate the average of a column
avg = df['Age'].mean()
print(f"Average of age: {avg}")

#Count the Unique values
uv = df['Age'].nunique()
print(f"unique values: {uv}")

#filter Rows based on a condition eg. filter all employees from engineering department
eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

#find the max, eg - get the employee with highest salary
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print("Highest paid employee : \n", max_salary_emp)

#find the min, eg - get the employee with lowest salary
min_salary = df['Salary'].min()
min_salary_emp = df[df['Salary'] == min_salary]
print("Minimum paid employee : \n", min_salary_emp)

#Count frequency of each value in a column, eg - count how many employeesare each department
dep_count = df['Department'].value_counts()
print("Number of employees in each department: \n",dep_count)

#sort data by column
sort = df.sort_values(by='Age', ascending=False)
print("Senior juinor employee: \n",sort)

#add a new column base on a condition eg- add experince based on age
df['Experience'] = df['Age'].apply(lambda x :'Senior' if x>=30 else 'Junior')
print("Data with Experience column: \n",df)


#data visualization

#plot a pie chart
plt.figure(figsize=(8,6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()
