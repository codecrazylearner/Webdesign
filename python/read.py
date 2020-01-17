import pandas as pd

sheets = pd.read_excel('queryresult.xlsx', sheet_name=['Sheet0', 'Sheet1', 'Sheet2','Sheet3', 'Sheet4',
                                                       'Sheet5', 'Sheet6', 'Sheet7', 'Sheet8', 'Sheet9'])
i = 0
name = ['Sheet0.csv', 'Sheet1.csv', 'Sheet2.csv', 'Sheet3.csv', 'Sheet4.csv',
        'Sheet5.csv', 'Sheet6.csv', 'Sheet7.csv', 'Sheet8.csv', 'Sheet9.csv']

for sheet in sheets:
    data_xls = pd.read_excel('queryresult.xlsx', sheet)
    filename = name[i]
    i = i + 1
    df1 = data_xls.to_csv(filename, encoding='utf-8')
