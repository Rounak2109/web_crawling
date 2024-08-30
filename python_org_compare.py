import pandas as pd
import numpy as np
import xlrd,xlsxwriter
df1 = pd.read_excel('python_org_jobs.xlsx')
df2 = pd.read_excel('python_org_jobs_recrawl.xlsx')
print(df1.equals(df2))

comparison_values=df1.values == df2.values
print (comparison_values)
rows,cols=np.where(comparison_values==False)

print(cols[1])
for item in zip(rows,cols):
    # print(rows)
    # print(item(cols))
    # if cols==9:
    if item[1] == 9:
        df2.iloc[item[0], item[1]] = '{}'.format(df1.iloc[item[0], item[1]])
    else:
         df2.iloc[item[0], item[1]] = '{}'.format(df2.iloc[item[0], item[1]])


print('Change is painful')
comparison_values=df1.values == df2.values
print(df2)
#print (comparison_values)
df2.to_excel('python_org_jobs.xlsx',index=False)