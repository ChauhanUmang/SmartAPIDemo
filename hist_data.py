from SmartApi import SmartConnect
from pyotp import TOTP
import cred as cd
import get_token as gt

# create object of call
obj = SmartConnect(api_key=cd.API_KEY)
# login api call
data = obj.generateSession(cd.CLIENT_CODE_Local, cd.PIN, TOTP(cd.totpCode).now())


# Keep this in mind that Angel API gives the starting time of the candle and not the closing time.
# e.g. the market opened at 9:15, and I want one-hour data. So typically I would expect the first candle to have a
# timestamp of 10:15 because 10:15 is when the first hour candle would be completed.

# However, instead of giving the end time for the candle, Angel One gives the starting time of the candle.

def get_hist_data(ticker, start_time, end_time, interval, exchange):
    params = {
        "exchange": exchange,
        "symboltoken": gt.get_token_value(),
        "interval": "THREE_MINUTE",
        "fromdate": "2021-02-10 09:15",
        "todate": "2021-02-10 09:16"
    }
    hist_data = obj.getCandleData(params)
