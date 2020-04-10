import pandas as pd

# The confirmed cases by country
data_url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
            'csse_covid_19_data/csse_covid_19_time_series'
            '/time_series_covid19_confirmed_global.csv')

df = pd.read_csv(data_url)
df.to_csv('covid-19-cases.csv')

# The number of deaths by country
data_url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
            'csse_covid_19_data/csse_covid_19_time_series'
            '/time_series_covid19_deaths_global.csv')

df = pd.read_csv(data_url)
df.to_csv('covid-19-deaths.csv')

# The confirmed cases in United States
data_loc_US=('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
           'csse_covid_19_data/csse_covid_19_time_series'
           '/time_series_covid19_confirmed_US.csv')
df_US_cases=pd.read_csv(data_loc_US)
df_US_cases.to_csv('covid-19-cases-US.csv')

# The deaths in the United States
data_loc_US_Deaths=('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
           'csse_covid_19_data/csse_covid_19_time_series'
           '/time_series_covid19_deaths_US.csv')

df_US_Deaths=pd.read_csv(data_loc_US_Deaths)
df_US_Deaths.to_csv('covid-19-deaths-US.csv')
