import csv
from binance.client import Client

client = Client("1zkB4N7AQCfR4pIm99zynO29OEQVAGmAitfaY0Xbu9a1ydqKiQVnuRR4u0OumHUh",
                "5IRwRHT2Kq89qE0iKG8fQfNPyhJrfzdBeq7K0Ke7xRbaQfS6WK1XkKfN5LJjJNBQ")

with open('pastdata.csv','w',newline='') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    for kline in client.get_historical_klines_generator("ETHBTC", Client.KLINE_INTERVAL_1MINUTE, "1 March, 2017"):
        wr.writerow([float(i) for i in kline])



