from binance.client import Client
import tensorflow as tf
from tensorflow import keras


new_model = keras.models.load_model('my_model.h5')

client = Client("1zkB4N7AQCfR4pIm99zynO29OEQVAGmAitfaY0Xbu9a1ydqKiQVnuRR4u0OumHUh",
                "5IRwRHT2Kq89qE0iKG8fQfNPyhJrfzdBeq7K0Ke7xRbaQfS6WK1XkKfN5LJjJNBQ")

order = client.order_market_buy(
    symbol='ETHBTC',
    quantity=30)