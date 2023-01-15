import pandas as pd
import requests

    
#data collection
url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data'
req = requests.get(url)
data_list = pd.read_html(req.text)
target_df = data_list[0]

#data cleaning
#column names
target_df.columns = ['col0','Country Name','Total Cases','Total Deaths','col4','col5','col6','col7']
#extra column
target_df = target_df[['Country Name','Total Cases','Total Deaths']]
#extra rows
last_idx = target_df.index[-1]
target_df = target_df.drop([last_idx])
#country name
target_df['Country Name'] = target_df['Country Name'].str.replace('\[.*\]','')
#no data
target_df['Total Deaths'] = target_df['Total Deaths'].str.replace('—','0')
#wrong data type
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])

#export the data
#target_df.to_csv(r'covid19_data.csv')
target_df.to_excel(r'covid19_data.xlsx')

