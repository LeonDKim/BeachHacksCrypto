from binance.client import Client

client= Client("1zkB4N7AQCfR4pIm99zynO29OEQVAGmAitfaY0Xbu9a1ydqKiQVnuRR4u0OumHUh",
                "5IRwRHT2Kq89qE0iKG8fQfNPyhJrfzdBeq7K0Ke7xRbaQfS6WK1XkKfN5LJjJNBQ")

import time
import win32api
gt = client.get_server_time()
tt=time.gmtime(int((gt["serverTime"])/1000))
win32api.SetSystemTime(tt[0],tt[1],0,tt[2],tt[3],tt[4],tt[5],0)
