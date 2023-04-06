# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:55:15 2023

@author: Kisha
"""
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def read_file(filename):
    
    worldbank = pd.read_csv(r'C:\Users\Kisha\OneDrive - University of Hertfordshire\Project 2\API_19_DS2_en_csv_v2_5361599.csv',skiprows=4)
    return worldbank


def filter_file(worldbank, column, value, countries, years):
    
    filtered_data = worldbank.groupby(column, group_keys=True)
    filtered_data = filtered_data.get_group(value)
    filtered_data = filtered_data.reset_index()
    filtered_data.set_index('Country Name', inplace=True)
    filtered_data = filtered_data.loc[:, years]
    filtered_data = filtered_data.loc[countries, :]
    filtered_data = filtered_data.dropna(axis=1)
    filtered_data = filtered_data.reset_index()
    transposed_data = filtered_data.set_index('Country Name')
    transposed_data = transposed_data.transpose()
    return filtered_data, transposed_data


def statis_data(dataframe, col, value, yr, a):
    
    df3 = dataframe.groupby(col, group_keys=True)
    df3 = df3.get_group(value)
    df3 = df3.reset_index()
    df3.set_index('Indicator Name', inplace=True)
    df3 = df3.loc[:, yr]
    df3 = df3.transpose()
    df3 = df3.loc[:, a]
    return df3



def line(dataset, title, xlab, ylab):
    
    dataset.plot.line(figsize=(50, 30), fontsize=60, linewidth=6.0)
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
    plt.title(title.upper(), fontsize=70, fontweight='bold')
    plt.xlabel(xlab, fontsize=70)
    plt.ylabel(ylab, fontsize=70)
    plt.legend(fontsize=40,loc='lower right')
    plt.show()
    return

country1 = ['India','Pakistan','China','United Kingdom']
year1 = ['1960', '1980', '2000', '2020']
world_data = read_file("climate_change.csv")
world_data1, transdata1 = filter_file(
    world_data, 'Indicator Name', 'CO2 emissions from solid fuel consumption (% of total)', country1, year1)
print(world_data1)
print(transdata1)

def bar(dataset, title, xlab, ylab):
    
    dataset.plot.bar(x='Country Name', rot=0, figsize=(50, 25),
                     fontsize=50)
    plt.yticks([0,20,40, 60, 80, 100])
    plt.legend(fontsize=50)
    plt.title(title.upper(), fontsize=50, fontweight='bold')
    plt.xlabel(xlab, fontsize=60)
    plt.ylabel(ylab, fontsize=60)
    plt.show()
    return

bar(world_data1, 'Total-CO2 from solid fuel consumption',
    'Countries', '% of CO2 emissions')

world_data2, transdata2 = filter_file(
    world_data, 'Indicator Name', 'Access to electricity (% of population)',
    country1, year1)
print(world_data2)
print(transdata2)
start = 2000
end = 2020
yeardes = [str(i) for i in range(start, end+1)]
indicator2 = ['Population growth (annual %)',
              'Electricity production from oil sources (% of total)',
              'Electricity production from nuclear sources (% of total)',
              'Electricity production from natural gas sources (% of total)']
descr = statis_data(world_data, 'Country Name',
                    'United Arab Emirates', yeardes, indicator2)
stats_summary = descr.describe()

print(stats_summary)
skewness = stats.skew(descr['Population growth (annual %)'])
kurtosis = descr['Electricity production from oil sources (% of total)'].kurtosis(
)
print('Skewness of Population growth in United Arab Emirates : ', skewness)
print('Kurtosis of Electricity production from natural gas in United Arab Emirates : ', kurtosis)
stats_summary.to_csv('statistics_report.csv')

bar(world_data2, 'population percent-Access to Electricity',
    'Countries', 'Percentage of Electricity access')
country2 = ['India','Pakistan','China','United Kingdom']
year2 = ['2000', '2005', '2010', '2015']
world_data3, transdata3 = filter_file(
    world_data, 'Indicator Name', 'Agricultural land (% of land area)',
    country2, year2)
print(transdata3)

line(transdata3, 'Area of Agricultural land',
     'Year', 'Agricultural land percentage')

world_data4, transdata4 = filter_file(
    world_data, 'Indicator Name',
    'Renewable energy consumption (% of total final energy consumption)',
    country2, year2)
print(world_data4)
print(transdata4)

line(transdata4, 'Total percent of Renewable energy consumption',
     'Year', '% of Renewable energy consumption')









