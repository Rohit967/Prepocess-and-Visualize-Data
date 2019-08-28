import pandas as pd
import matplotlib.pyplot as plt

#---- Step1:
# Please use read_csv function to import the dataset: dob_job_application_filings_subset.csv
df = pd.read_csv('dob_job_application_filings_subset.csv')

#---- Step2:
# Using .head(), .tail(), .info(), .describe() methods and .shape, .columns attributes to explore your data set

df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes

#df['Initial Cost'].str.replace('$', '')
#df['Total Est. Fee'].str.replace('$', '')

#describing the interesting things i found
# analzye using .info()
'''
print(df['Applicant Professional Title'].value_counts(dropna=True))
print(df['Borough'].value_counts(dropna=False))
print(df['State'].value_counts(dropna=False))
print(df['eFiling Filed'].value_counts(dropna=False))
print(df['Site Fill'].value_counts(dropna=False))
print(df['Job Type'].value_counts(dropna=False))
print(df['Job Status'].value_counts(dropna=False))
print(df['Professional Cert'].value_counts(dropna=False))
print(df['Fee Status'].value_counts(dropna=False))
print(df['Latest Action Date'].value_counts(dropna=False))
'''

#---- Step3:
# Removing the "$" sign from the column 'Initial Cost' and the column 'Total Est. Fee' 
df['Initial Cost'] = df['Initial Cost'].str.replace("$", "")
df['Total Est. Fee']= df['Total Est. Fee'].str.replace("$", "")

#tips['total_bill'] = tips['total_bill'].str.replace("$","")
#tips['tip'] = tips['tip'].str.replace("$","")

#---- Step4:
#convert the type of the column 'Initial Cost' and  the column 'Total Est. Fee' to numeric numbers.
df['Initial Cost'] = pd.to_numeric(df['Initial Cost'], errors ='coerce')
df['Total Est. Fee'] = pd.to_numeric(df['Total Est. Fee'], errors='coerce')

#df[['Initial Cost', 'Total Est. Fee']].apply(pd.to_numeric,errors='coerce').dtypes
#print(df.info())

# Print the info of tips
print(df.info())


# Step 5:
#Please plot the boxplot how  'Initial Cost'  varies by 'Borough', and describe the interesting thing you find.
df.boxplot(column='Borough', by='Initial Cost', rot=90)
plt.show()


df['Initial Cost'].plot('hist')
plt.show()

df[df['Initial Cost'] > 1000000000]

#Boxplot can find outlier
df.boxplot(column='Initial Cost',by='Borough')
plt.show()

##
import pandas as pd
import matplotlib.pyplot as plt
def convert_currency(val):
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

df = pd.read_csv('dob_job_application_filings_subset.csv')
s1 = df['Initial Cost'].apply(convert_currency)
s2 = df['Borough']

dt = (s1,s2)
print(dt)

mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)

dt.boxplot(column = s1,by = s2)

plt.boxplot(dt)


# Step 6
#Please plot the scatter plot between the column 'Initial Cost' and the column 'Total Est. Fee', and describe 
#the interesting thing you find, please label the interesting data point you find in the figure.
t1 = df['Initial Cost'].apply(convert_currency)
t2 = df['Total Est. Fee'].apply(convert_currency)

plt.scatter(t1, t2, marker='o')

##
import pandas as pd
import matplotlib.pyplot as plt

df.plot(kind='scatter', x='Initial Cost', y='Total Est. Fee', rot=70)
plt.show()

# Data Visualisation

df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
plt.show()

# boxplots

df.plot(kind='scatter', x='Proposed Height', y='Existing Zoning Sqft', rot=70)
plt.show()
