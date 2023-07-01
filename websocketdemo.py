from SmartApi import SmartConnect
from pyotp import TOTP
import get_token as gt
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
import cred as cd
from decimal import Decimal

# create object of call
obj = SmartConnect(api_key=cd.API_KEY)
# login api call
data = obj.generateSession(cd.CLIENT_CODE_Local, cd.PIN, TOTP(cd.totpCode).now())
feedToken = obj.getfeedToken()

AUTH_TOKEN = data['data']['jwtToken']
API_KEY = cd.API_KEY
CLIENT_CODE = cd.CLIENT_CODE_Local
FEED_TOKEN = feedToken

correlation_id = "socket1"
action = 1
mode = 1

token_list = [{"exchangeType": 1, "tokens": ["26009", "11536", "1594", "8110"]}]

sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))
    ltp = Decimal(message['last_traded_price'])/100
    print(ltp)
    if message['token'] == '11536' and ltp > 3210:
        print("buy TCS")


def on_open(wsapp):
    print("on open")
    sws.subscribe(correlation_id, mode, token_list)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()




