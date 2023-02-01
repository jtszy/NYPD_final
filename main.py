import argparse

import analiza

'''
Plik obslugujacy analize danych z zainstalowanym pakietem 'analiza'
'''

parser = argparse.ArgumentParser()

parser.add_argument(
    'start_year',
    help = 'start year for analysis, default equal 2000',
    type=int,
    nargs='?',
    default=2000
)

parser.add_argument(
    'end_year',
    help = 'end year for analysis default equal 2004',
    type=int,
    nargs='?',
    default=2004
)

parser.add_argument(
    'gdp_path',
    help="path to GDP csv file, if blank it's egual '/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'",
    nargs='?',
    type = str,
    default='/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'
)

parser.add_argument(
    'pop_path',
    help="path to population csv file, if blank it's '/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'",
    nargs='?',
    default='/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'
)

parser.add_argument(
    'co2_path',
    help="path to CO2 csv file, if blank it's '/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv'",
    nargs='?',
    default='/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv'
)

args = parser.parse_args()

assert args.start_year <= args.end_year, "Niepoprawny przedzial lat"

# wczytanie parametrow z zadanych sciezek
gdp_data, pop_data, co2_data = analiza.reading_data(args.gdp_path, args.pop_path, args.co2_path)

# scalenie danych
merged_data = analiza.merging_data(gdp_data, pop_data, co2_data)

# największa emisja CO2 na mieszkańca
analiza.most_co2(args.start_year, args.end_year, merged_data)

# najekszy przychod na mieszkanca
analiza.most_gdp(args.start_year, args.end_year, merged_data)

# najwieksza zmiana w przeciagu ostatnich 10 lat
analiza.biggest_change(merged_data)
