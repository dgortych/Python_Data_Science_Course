import requests

data_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-08.parquet'

response = requests.get(data_url)
open('taxi.parquet', 'wb').write(response.content)        