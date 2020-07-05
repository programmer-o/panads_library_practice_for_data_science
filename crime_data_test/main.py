import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('SacramentocrimeJanuary2006.csv')
print(df)
profile = ProfileReport(df)
profile.to_file(output_file='result.html')