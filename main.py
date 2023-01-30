import numpy as np
import pandas as pd
import os


'''
Pobieranie tekstu
'''

current_path = os.getcwd()

path = current_path + "/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv"

gpd_data = pd.read_csv(path, header = 2)

gpd_data_columns = gpd_data.columns
# print(gpd_data_columns)

del gpd_data['Country Code']
del gpd_data['Indicator Name']
del gpd_data['Indicator Code']
del gpd_data['Unnamed: 66']

gpd_data['data_type'] = pd.Series('gpd',index = range(266))


print(gpd_data.head())

print()

path = current_path + "/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv"

pop_data = pd.read_csv(path, header = 2)

pop_data_columns = pop_data.columns
# print(pop_data_columns)

del pop_data['Country Code']
del pop_data['Indicator Name']
del pop_data['Indicator Code']
del pop_data['Unnamed: 66']

pop_data['data_type'] = pd.Series('pop',index = range(266))

print(pop_data.head())

path = current_path + "/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv"

co2_data = pd.read_csv(path)

co2_data_columns = co2_data.columns
# print(co2_data_columns)

co2_data = co2_data[co2_data_columns[0:3]]

# print(co2_data.head())

co2_pivot = pd.pivot_table(
    data = co2_data,
    index = 'Country',
    columns = 'Year'
)

co2_index_list = list(co2_pivot.index)

'''
Uzyskanie tego sameg formatu danych: zmiana nazw państw i uzyskanie wspólnych krajów
'''








'''
Ustalenie wspólnego zakresu lat
'''

'''
Scalanie danych
'''
#Oczyścić lata z krajów kiedyś, scalić po krajach 3 tabele i przeprowadzać analizy

countries = gpd_data[gpd_data_columns[0]].tolist() #takie same jak dla pop_data

# a = [i//2 for i in range(len(countries)*2)]
# b = [i%2 for i in range(len(countries)*2)]
#
# midx = pd.MultiIndex(levels = [countries, ['gpd','pop']], codes = [a,b])

concat_dataframe = pd.concat([gpd_data, pop_data])

merged_dataframes = concat_dataframe.groupby(['Country Name', 'data_type']).mean()

print(merged_dataframes.loc['Aruba'])

def compare(list1, list2):
    for x in range(len(list1)):
        if not list1[x] in list2:
            print(x,list1[x])

def converte(capital_string):
    res = ''
    capital_letter = True
    for char in capital_string:
        if capital_letter and char != char.lower():
            capital_letter = False
            res += char
            continue
        if char == " ":
            capital_letter = True
        res += char.lower()
    return res

co2_index_list = [converte(item) for item in co2_index_list]
# print(co2_index_list)




path = current_path + '/world-countries/countries/en/countries.csv'

country_list = pd.read_csv(path)['name'].tolist()


regions_to_drop = [1,3,7,11,27,36,38,49,61,62,63,64,65,68,73,74,84,91,93,96,98,102,103,104,105,107,108,110,128,134,135,136,139,
                   140,142,146,147,153,156,161,164,170,172,181,183,191,192,196,197,198,199,204,215,217,218,225,228,230,231,236,
                   238,240,241,249,255,256,259,261]

for i in regions_to_drop:
    merged_dataframes = merged_dataframes.drop(countries[i])

for x in merged_dataframes.index:
    print(x)



