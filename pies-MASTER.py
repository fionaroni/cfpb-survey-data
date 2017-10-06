import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xl = pd.ExcelFile("Customer_Survey_Data.xlsx")
df = xl.parse("Survey Data")

df.info()

# Pie charts on entire dataset

# Racial makeup Pie
counts_race = df['Race'].value_counts()
colors = ['#0055D4','#0071C6','#008DB8','#00AAAA','#00C69C','#00E28E','#00FF80']
explode = (0.005, 0.005, 0.005, 0.005, 0.005, 0.005)
plt.axis('equal')
counts_race.plot(kind='pie', fontsize=14, colors=colors, explode=explode, autopct='%1.1f%%')
plt.legend(labels=counts_race.index, loc=3)
plt.title("Race", fontsize=20)
plt.axis('off')
plt.show()

# Education Pie
counts_educ = df['Highest Education Achieved'].value_counts()
colors = ['#800080','#9400D3','#8A2BE2','#9966CC','#BA55D3','#DA70D6','#EE82EE','#DDA0DD', '#D8BFD8', '#E6E6FA']
explode = (0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.2)
plt.axis('equal')
counts_educ.plot(kind='pie', fontsize=14, colors=colors, explode=explode, autopct='%1.1f%%', pctdistance=0.8)
plt.legend(labels=counts_educ.index, loc=3)
plt.title("Highest Education Achieved", fontsize=20)
plt.axis('off')
plt.show()

# Employment Status Pie
counts_empl = df['Employment Type'].value_counts()
colors = ['#FFA500','#FF8C00','#FF4500','#FF6347','#FF7F50', '#FFA07A']
plt.axis('equal')
counts_empl.plot(kind='pie', fontsize=14, colors=colors, autopct='%1.1f%%')
plt.legend(labels=counts_empl.index, loc=3)
plt.title("Employment Status", fontsize=20)
plt.axis('off')
plt.show()

