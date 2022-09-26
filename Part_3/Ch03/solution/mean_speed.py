# What is the mean speed (mile/hour) in taxi.csv?

# - Run download_data.py to download the data

# %%
import pandas as pd

time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]

df = data = pd.read_parquet(r'D:\Projekty Python\Kurs_Linkedin_Python_for_Data_science\Part_3\Ch03\challenge\taxi.parquet', engine='pyarrow')

times = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
times_hour = times / pd.Timedelta(1, 'hour')
speed = df['trip_distance'] / times_hour
speed.mean()