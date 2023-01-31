import os

import pandas as pd

import dwl


def reading_data(gdp_path,pop_path,co2_path):
    '''
    wczytywanie baz danych do analizy
    zwraca 3 data framy
    '''

    current_path = os.getcwd()

    # wczytywanie danych o PKB
    path = current_path + gdp_path

    gdp_data = pd.read_csv(path, header=2)

    del gdp_data['Country Code']
    del gdp_data['Indicator Name']
    del gdp_data['Indicator Code']
    del gdp_data['Unnamed: 66']

    gdp_data['data_type'] = pd.Series('gdp', index=gdp_data.index)

    # wczytywanie danych o populacji
    path = current_path + pop_path

    pop_data = pd.read_csv(path, header=2)

    del pop_data['Country Code']
    del pop_data['Indicator Name']
    del pop_data['Indicator Code']
    del pop_data['Unnamed: 66']

    pop_data['data_type'] = pd.Series('pop', index=pop_data.index)

    # wczytywanie danych o emisji co2
    path = current_path + co2_path

    co2_data = pd.read_csv(path)

    co2_data = co2_data[co2_data.columns[0:3]]

    co2_data = pd.pivot_table(
        data=co2_data,
        index='Country',
        columns='Year'
    )

    co2_data.columns = co2_data.columns.droplevel(0)
    co2_data['data_type'] = pd.Series('co2', index=co2_data.index)

    return gdp_data, pop_data, co2_data


def merging_data(gdp_data, pop_data, co2_data):
    '''
    łaczenie wcześniej wczytanych danych
    '''

    countries = gdp_data[gdp_data.columns[0]].tolist()
    # lista krajow, taka sama jak dla pop_data

    gdp_pop_regions_drop = [0, 1, 3, 7, 11, 27, 36, 38, 49, 51, 52, 61, 62, 63, 64, 65, 68, 73, 74, 84, 91, 93, 95, 96,
                            98, 102,
                            103, 104, 105, 107, 108, 110, 128, 134, 135, 136, 139, 140, 142, 146, 147, 153, 156, 161,
                            164, 170,
                            172, 181, 183, 191, 192, 196, 197, 198, 199, 204, 215, 217, 218, 225, 228, 230, 231, 236,
                            238, 240,
                            241, 249, 255, 256, 259, 261]
    # obszary do odrzucenia z tabeli z pkb i populacja, ktore nie sa krajami

    co2_index_list = list(co2_data.index)
    co2_index_list = [dwl.converte(item) for item in co2_index_list]
    # zmiana wielkich liter w zapisie panstw

    co2_regions_drop = [5, 6, 10, 22, 24, 28, 36, 41, 45, 50, 53, 61, 70, 71, 72, 73, 76, 77, 78, 79, 80, 81, 82, 83,
                        84, 85, 91,
                        93, 95, 102, 114, 120, 125, 126, 132, 141, 147, 154, 155, 157, 162, 164, 172, 175, 178, 184,
                        186, 187, 191,
                        192, 193, 193, 196, 199, 214, 215, 223, 225, 240, 244, 248, 249, 251, 252, 254]

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
    # zmiana nazwy krajow w zestawieniu produkcji CO2

    # powyzsze dane znalezione przy uzyciu funkcji compare z modulu dwl

    for i in gdp_pop_regions_drop[::-1]:
        gdp_data = gdp_data.drop(i)
        pop_data = pop_data.drop(i)
        del countries[i]
    # odrzucene wskazanych regionow

    co2_data.columns = [str(x) for x in co2_data.columns]

    co2_data.index = co2_index_list
    co2_data.index = co2_data.index.rename('Country Name')

    for i in co2_regions_drop[::-1]:
        co2_data = co2_data.drop(co2_index_list[i])
        del co2_index_list[i]
    # odrzucenie wskazanych regionow

    co2_data = co2_data.reset_index()

    start_year = max(int(gdp_data.columns[1]), int(pop_data.columns[1]), int(co2_data.columns[1]))
    end_year = min(int(gdp_data.columns[-2]), int(pop_data.columns[-2]), int(co2_data.columns[-2]))
    years = [str(i) for i in range(start_year, end_year + 1)]
    # ustalenie wspolnego przedzialu lat

    co2_data = pd.concat([co2_data['Country Name'], co2_data[years], co2_data['data_type']], axis=1)
    gdp_data = pd.concat([gdp_data['Country Name'], gdp_data[years], gdp_data['data_type']], axis=1)
    pop_data = pd.concat([pop_data['Country Name'], pop_data[years], pop_data['data_type']], axis=1)
    # obciecie kolumn do ustalonego przedzialu

    merged_dataframes = pd.concat([gdp_data, pop_data, co2_data]).groupby(['Country Name', 'data_type']).mean()
    # polaczenie tabeli

    return merged_dataframes


def most_co2(start_year, end_year, data):
    '''
    pierwsza analiza - największa emisja CO2 na mieszkańca, w zadanym przedziale czasowym
    '''

    print('Największy emisja CO2 na mieszkanca w latach ', start_year, ' - ', end_year, ':')

    columns = [str(year) for year in range(start_year, end_year + 1)]
    res_all_years = pd.DataFrame(columns=columns)
    # zdefiniowanie dataframu dla podanych lat

    for row in data.index.get_level_values(0).drop_duplicates():
        if ('co2' in data.loc[row].index) and ('pop' in data.loc[row].index):
            res_all_years.loc[row] = data.loc[row].loc['co2'] / data.loc[row].loc['pop']
    # uzupelnienie ilorazem emisji CO2 przez populacje

    for year in columns:
        res = res_all_years[year].nlargest(5).rename('co2_per_capita_' + year)
        res = pd.concat([res, data[year].loc[res.index].loc[:, 'co2'].rename('total_co2_' + year)], axis=1)
        print(res, '\n')
    # wybranie 5 największych rekordów w odpowiednich latach


def most_gdp(start_year, end_year, data):
    '''
    druga analiza - najekszy przychod na mieszkanca, w zadanym przedziale czasowym
    '''

    print('Największy przychod na mieszkanca w latach ', start_year, ' - ', end_year, ':')

    columns = [str(year) for year in range(start_year, end_year + 1)]
    res_all_years = pd.DataFrame(columns=columns)
    # zdefiniowanie dataframu dla podanych lat


    for row in data.index.get_level_values(0).drop_duplicates():
        if ('gdp' in data.loc[row].index) and ('pop' in data.loc[row].index):
            res_all_years.loc[row] = data.loc[row].loc['gdp'] / data.loc[row].loc['pop']
    # uzupelnienie ilorazem PKB przez populacje

    for year in columns:
        res = res_all_years[year].nlargest(5).rename('gdp_per_capita_' + year)
        res = pd.concat([res, data[year].loc[res.index].loc[:, 'gdp'].rename('total_gdp_' + year)], axis=1)
        print(res, '\n')
    # wybranie 5 największych rekordów w odpowiednich latach



def biggest_change(data):
    '''
    trzecia analiza - najwieksza zmiana w przeciagu ostatnich 10 lat pod wzgledem produkcji CO2
    '''

    change = data[data.columns[-2]] - data[data.columns[-12]]
    # kolumna różnic przez ostatnie 10 lat

    print('Najwiekszy wzrost emisji:', '\n', change.loc[:, 'co2'].nlargest(5), '\n')
    print('Największe ograniczenie emisji:', '\n', change.loc[:, 'co2'].nsmallest(5))
    # wybranie 5 największych pozytywnych i negatywnych zmian w emisji CO2
