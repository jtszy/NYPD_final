import numpy as np
import pandas as pd
import os
import dwl

'''
Pobieranie tekstu
'''

current_path = os.getcwd()

path = current_path + "/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv"

gdp_data = pd.read_csv(path, header=2)

gdp_data_columns = gdp_data.columns
# print(gdp_data_columns)

del gdp_data['Country Code']
del gdp_data['Indicator Name']
del gdp_data['Indicator Code']
del gdp_data['Unnamed: 66']

gdp_data['data_type'] = pd.Series('gdp', index=range(266))

# print(gdp_data.head())


path = current_path + "/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv"

pop_data = pd.read_csv(path, header=2)

pop_data_columns = pop_data.columns
# print(pop_data_columns)

del pop_data['Country Code']
del pop_data['Indicator Name']
del pop_data['Indicator Code']
del pop_data['Unnamed: 66']

pop_data['data_type'] = pd.Series('pop', index=range(266))

# print(pop_data.head())

path = current_path + "/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv"

co2_data = pd.read_csv(path)

co2_data = co2_data[co2_data.columns[0:3]]

# print(co2_data.head())

co2_pivot = pd.pivot_table(data=co2_data, index='Country', columns='Year')

co2_index_list = list(co2_pivot.index)
#ładowanie danych

#ustaleneie przedziału lat


'''
Uzyskanie tego sameg formatu danych: zmiana nazw państw i uzyskanie wspólnych krajów
'''

'''
Ustalenie wspólnego zakresu lat
'''

'''
Scalanie danych
'''
# Oczyścić lata z krajów kiedyś, scalić po krajach 3 tabele i przeprowadzać analizy

countries = gdp_data[gdp_data_columns[0]].tolist()  # takie same jak dla pop_data

# a = [i//2 for i in range(len(countries)*2)]
# b = [i%2 for i in range(len(countries)*2)]
#
# midx = pd.MultiIndex(levels = [countries, ['gdp','pop']], codes = [a,b])

concat_dataframe = pd.concat([gdp_data, pop_data])

merged_dataframes = concat_dataframe.groupby(['Country Name', 'data_type']).mean()

print(merged_dataframes.loc['Aruba'])

co2_index_list = [dwl.converte(item) for item in co2_index_list]
# print(co2_index_list)


# PORÓWNANIE DANYCH Z BANKU ŚWIATOWEGO Z LISTĄ KRAJÓW, ABY WYRZUCIĆ OBSZARY, KTÓRE NIE SĄ KRAJAMI
'''
path = current_path + '/world-countries/countries/en/countries.csv'

country_list = pd.read_csv(path)['name'].tolist()

dwl.compare(countries,country_list)
'''

regions_to_drop = [0, 1, 3, 7, 11, 27, 36, 38, 49, 51, 52, 61, 62, 63, 64, 65, 68, 73, 74, 84, 91, 93, 95, 96, 98, 102,
                   103, 104, 105, 107, 108, 110, 128, 134, 135, 136, 139, 140, 142, 146, 147, 153, 156, 161, 164, 170,
                   172, 181, 183, 191, 192, 196, 197, 198, 199, 204, 215, 217, 218, 225, 228, 230, 231, 236, 238, 240,
                   241, 249, 255, 256, 259, 261]

# czyszczenie danych z obszarow, ktore nie sa krajami

for i in regions_to_drop[::-1]:
    merged_dataframes = merged_dataframes.drop(countries[i])
    del countries[i]

columns = [str(i) for i in range(1960, 2022)]
res_1 = pd.DataFrame(columns=columns)

for row in countries:
    res_1.loc[row] = merged_dataframes.loc[row].loc['gdp'] / merged_dataframes.loc[row].loc['pop']

year = '2021'

res_of_first = res_1[year].nlargest(5).rename('gdp_per_capita_' + year)

res_of_first = pd.concat(
    [res_of_first, merged_dataframes[year].loc[res_of_first.index].loc[:, 'gdp'].rename('total_gdp_' + year)], axis=1)

# print(res_of_first)

# print(pd.concat([gdp_data, pop_data, co2_pivot]))

# dwl.compare(co2_index_list, countries)

co2_index_list[14] = 'Bahamas, The'
co2_index_list[29] = 'Brunei Darussalam'
co2_index_list[35] = 'Cabo Verde'
co2_index_list[40] = 'China'
co2_index_list[44] = 'Congo, Rep.'
co2_index_list[47] = "Cote d'Ivoire"
co2_index_list[52] = 'Czechia'
co2_index_list[54] = "Korea, Dem. People's Rep."
co2_index_list[55] = 'Congo, Dem. Rep.'
co2_index_list[56] = 'Vietnam'
co2_index_list[63] = 'Egypt, Arab Rep.'
co2_index_list[69] = 'Faroe Islands'
co2_index_list[72] = 'Micronesia, Fed. Sts.'
co2_index_list[80] = 'France'
co2_index_list[87] = 'Gambia, The'
co2_index_list[98] = 'Guinea-Bissau'
co2_index_list[109] = 'Iran, Islamic Rep.'
co2_index_list[111] = 'Italy'
co2_index_list[121] = 'Kyrgyz Republic'
co2_index_list[122] = 'Lao PDR'
co2_index_list[124] = 'Palau'
co2_index_list[128] = 'Libya'
co2_index_list[133] = 'North Macedonia'
co2_index_list[150] = 'Myanmar'
co2_index_list[166] = 'Palau'
co2_index_list[180] = 'Cameroon'
co2_index_list[181] = 'Korea, Rep.'
co2_index_list[182] = 'Moldova'
co2_index_list[183] = 'South Sudan'
co2_index_list[185] = 'Sudan'
co2_index_list[195] = 'St. Lucia'
co2_index_list[206] = 'Slovak Republic'
co2_index_list[213] = 'St. Kitts and Nevis'
co2_index_list[216] = 'St. Vincent and the Grenadines'
co2_index_list[219] = 'Eswatini'
co2_index_list[227] = 'Timor-Leste'
co2_index_list[230] = 'Trinidad and Tobago'
co2_index_list[232] = 'Turkiye'
co2_index_list[234] = 'Turks and Caicos Islands'
co2_index_list[241] = 'Tanzania'
co2_index_list[242] = 'United States'
co2_index_list[247] = 'Venezuela, RB'
co2_index_list[250] = 'Yemen, Rep.'

regions_to_drop_co2 = [5,6,10,22,24,28,36,41,45,50,53,61,70,71,72,73,76,77,78,79,80,81,82,83,84,85,91,
                       93,95,102,114,120,125,126,132,141,147,154,155,157,162,164,172,175,178,184,186,187,191,
                       192,193,193,196,199,214,215,223,225,240,244,248,249,251,252,254]

co2_pivot.columns = co2_pivot.columns.droplevel(0)
co2_pivot.index = co2_index_list
co2_pivot.index = co2_pivot.index.rename('Country Name')
co2_pivot.columns = [str(x) for x in co2_pivot.columns]

for i in regions_to_drop_co2[::-1]:
    co2_pivot = co2_pivot.drop(co2_index_list[i])
    del co2_index_list[i]

co2_pivot = co2_pivot.reset_index()

co2_pivot['data_type'] = pd.Series('co2', index=range(len(co2_index_list)))

start_year = max(int(gdp_data.columns[1]), int(pop_data.columns[1]), int(co2_pivot.columns[1]))

end_year = min(int(gdp_data.columns[-2]), int(pop_data.columns[-2]), int(co2_pivot.columns[-2]))

years = [str(i) for i in range(start_year,end_year+1)]

co2_pivot = pd.concat([co2_pivot['Country Name'],co2_pivot[years],co2_pivot['data_type']], axis = 1)
gdp_data = pd.concat([gdp_data['Country Name'],gdp_data[years],gdp_data['data_type']], axis = 1)
pop_data = pd.concat([pop_data['Country Name'],pop_data[years],pop_data['data_type']], axis = 1)

merged_dataframes = pd.concat([gdp_data,pop_data,co2_pivot]).groupby(['Country Name', 'data_type']).mean()

print(merged_dataframes)











