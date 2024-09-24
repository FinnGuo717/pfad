from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

url="https://www.data.jma.go.jp/env/kosahp/kosa_table_0.html"
response = requests.get(url)

if response.ok:
    print("Data is ready")

    soup = bs(response.text,'html.parser')
    table = soup.find('table') 

table_str = str(table)

table_io = StringIO(table_str)

df = pd.read_html(table_io, header=1)[0]

df = df.rename(columns={'2024': 'year', 'Unnamed: 1': '1月','Unnamed: 2': '2月','Unnamed: 3': '3月','Unnamed: 4': '4月','Unnamed: 5': '5月','Unnamed: 6': '6月','Unnamed: 7': '7月','Unnamed: 8': '8月','Unnamed:8': '8月','Unnamed: 9': '9月','Unnamed: 10': '10月','Unnamed: 11': '11月','Unnamed: 12': '12月','0': 'Summary'})

columns = df.columns

df_summary = df[['year', 'Summary']]

df_summary.plot(x='year', y='Summary', kind='bar', legend=False)

plt.title('Yearly Summary Data')
plt.xlabel('Year')
plt.ylabel('Summary')

plt.show()