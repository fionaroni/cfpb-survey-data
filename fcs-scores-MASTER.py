import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xl = pd.ExcelFile("Customer Survey Data w Data Dictionary.xlsx")
df = xl.parse("Survey Data")

df.info()

# Histogram on FCS Scores - all customers
df['FCS Score'].plot(kind='hist', alpha=0.5, bins=9, range=(0,9), normed=True)
mean = np.around(df['FCS Score'].mean(), decimals=2)
stdev = np.around(df['FCS Score'].std(), decimals=2)
plt.xlabel('FCS Score')
plt.ylabel('Probability Density')
plt.grid(b=True, which='minor', color='.065', linestyle='-')
plt.xticks([0,1,2,3,4,5,6,7,8,9])
plt.title(f'Histogram of FCS Scores \n$\mu={mean}$, $\sigma={stdev}$')
plt.show()

plt.clf

# Histogram on FCS Scores - by education achieved
df['FCS Score'].hist(by=df['Highest Education Achieved'], bins=9, range=(0,9), normed=True)
plt.show()

# Histogram on FCS Scores - by employment
df['FCS Score'].hist(by=df['Employment Type'], bins=9, range=(0,9), normed=True)
plt.show()

# Histogram on FCS Scores - by race 
df['FCS Score'].hist(by=df['Race'], bins=9, range=(0,9), normed=True, stacked=True)
plt.show()

# Overlaid Histograms of FCS Scores by Race
df0 = df[df['Race'] == 'Black/African-American']['FCS Score'].dropna()
df1 = df[df['Race'] == 'White/Caucasian']['FCS Score'].dropna()
df2 = df[df['Race'] == 'Multiracial']['FCS Score'].dropna()
df3 = df[df['Race'] == 'American Indian or Alaska Native']['FCS Score'].dropna()
df4 = df[df['Race'] == 'Asian or Pacific Islander']['FCS Score'].dropna()

fig, ax = plt.subplots()
ax.hist(df0, bins=9, range=(0,9), color='m', histtype='step', label='Black/African-American')
ax.hist(df1, bins=9, range=(0,9), color='y', histtype='step', label='White/Caucasian')
ax.hist(df2, bins=9, range=(0,9), color='c', histtype='step', label='Multiracial')
ax.hist(df3, bins=9, range=(0,9), color='b', histtype='step', label='American Indian or Alaska Native')
ax.hist(df4, bins=9, range=(0,9), color='k', histtype='step', label='Asian or Pacific Islander')

ax.legend(loc='upper right')
plt.title('FCS Score by Race')
plt.ylabel('Number of Survey Respondents')
plt.xlabel('FCS Score')
plt.show()


