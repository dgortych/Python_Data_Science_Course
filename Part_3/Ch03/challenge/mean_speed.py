# What is the mean speed (mile/hour) in taxi.csv?

# - Run download_data.py to download the data

# %%
import pandas as pd
data = pd.read_parquet(r'D:\Projekty Python\Kurs_Linkedin_Python_for_Data_science\Part_3\Ch03\challenge\taxi.parquet', engine='pyarrow')

data.head(10)

# %%

data.describe()
# %%
data.info()


data['time'] = data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']

data['time'].head()
# %%
xd = pd.Timedelta(1, 'hour')
data['time'] = data['time'] / xd
data['time'].head()

# %%
data['speed'] = data['trip_distance'] / data['time']
data['speed'].head(20)

# %%
data_new = data.query('speed > 0.0 and speed < 99999 ')
data_new['speed'].describe()