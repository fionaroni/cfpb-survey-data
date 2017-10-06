import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xl = pd.ExcelFile("Customer Survey Data w Data Dictionary.xlsx")
df = xl.parse("Survey Data")


# Convert categorical survey data to numeric values, according to scoring guide
# (available at http://files.consumerfinance.gov/f/201512_cfpb_financial-well-being-worksheet-standard.pdf)
def convert_completely(categorical_col):			
	'''Create a new column with numeric data that corresponds to categorical data in an existing column.'''
	numeric_col = categorical_col.map({'Completely': 4, 'Very Well': 3, 'Somewhat': 2, 'Very Little': 1, 'Not at All': 0})
	return numeric_col

def convert_completely_reverse(categorical_col):			
	'''Create a new column with numeric data that corresponds to categorical data in an existing column.'''
	numeric_col = categorical_col.map({'Completely': 0, 'Very Well': 1, 'Somewhat': 2, 'Very Little': 3, 'Not at All': 4})
	return numeric_col

def convert_always(categorical_col):				
	'''Create a new column with numeric data that corresponds to categorical data in an existing column.'''
	numeric_col = categorical_col.map({'Always': 4, 'Often': 3, 'Sometimes': 2, 'Rarely': 1, 'Never': 0})
	return numeric_col

def convert_always_reverse(categorical_col):				
	'''Create a new column with numeric data that corresponds to categorical data in an existing column.'''
	numeric_col = categorical_col.map({'Always': 0, 'Often': 1, 'Sometimes': 2, 'Rarely': 3, 'Never': 4})
	return numeric_col


for i in df.iloc[:, 9:19]:# Loop over CFPB_Q1 through CFPB_Q10		
	if int(i[-1]) >= 7: # Q7, Q8, Q9
		numeric_col_name = 'numeric_CFPB_Q' + i[-1]			# Create new column name				
		if i[-1] == '8': # Q8				
			df[numeric_col_name] = convert_always(df[i])		# Generate column data containing numeric representations of survey responses
		else: # Q7, Q9
			df[numeric_col_name] = convert_always_reverse(df[i])	
	else:
		if i[-2:] == '10': # Q10	
			numeric_col_name = 'numeric_CFPB_Q' + i[-2:]		
			df[numeric_col_name] = convert_always_reverse(df[i])
		elif int(i[-1]) == 3 or int(i[-1]) == 5 or int(i[-1]) == 6: # Q3, Q5, Q6								
			numeric_col_name = 'numeric_CFPB_Q' + i[-1]							
			df[numeric_col_name] = convert_completely_reverse(df[i])
		else: # Q1, Q2, Q4
			numeric_col_name = 'numeric_CFPB_Q' + i[-1]				
			df[numeric_col_name] = convert_completely(df[i])	

for i in df:
	print(i)

# Test for loop: print statements
print('Completely: 1, 2, 4')
print(df.loc[:,['CFPB_Q1','numeric_CFPB_Q1']])
print(df.loc[:,['CFPB_Q2','numeric_CFPB_Q2']])
print(df.loc[:,['CFPB_Q4','numeric_CFPB_Q4']])

print('Completely reverse: 3, 5, 6')
print(df.loc[:,['CFPB_Q3','numeric_CFPB_Q3']])
print(df.loc[:,['CFPB_Q5','numeric_CFPB_Q5']])
print(df.loc[:,['CFPB_Q6','numeric_CFPB_Q6']])

print('Always: 8')
print(df.loc[:,['CFPB_Q8','numeric_CFPB_Q8']])

print('Always reverse: 7, 9, 10')
print(df.loc[:,['CFPB_Q7','numeric_CFPB_Q7']])
print(df.loc[:,['CFPB_Q9','numeric_CFPB_Q9']])
print(df.loc[:,['CFPB_Q10','numeric_CFPB_Q10']])

# Calculate CFPB Response Value, store in new column
CFPB_columns = list(df)[-10:]
print(CFPB_columns)
df['CFPB Response Value'] = df[CFPB_columns].sum(axis=1)


writer = pd.ExcelWriter('CFPB-withRV.xlsx')
df.to_excel(writer, 'Survey Data w CFPB R Value')
writer.save()
writer.close()



