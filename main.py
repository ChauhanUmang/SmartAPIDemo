from SmartApi import SmartConnect
from pyotp import TOTP
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
# from smartapi.smartWebSocketV2 import SmartWebSocketV2
import pandas as pd
import requests
import datetime
import get_token as gt
import cred as cd


# create object of call
obj = SmartConnect(api_key=cd.API_KEY,
                   # optional
                   # access_token = "your access token",
                   # refresh_token = "your refresh_token"
                   )

# login api call
data = obj.generateSession(cd.CLIENT_CODE_Local, cd.PIN, TOTP(cd.totpCode).now())
# refreshToken = data['data']['refreshToken']

token_df = gt.get_token_df()

sp_list = [42500, 43000, 43500, 44000, 44500]

for i in sp_list:
    token_row = gt.get_token_value(df=token_df, CE_PE="CE", strike_price=i)
    print(f"Token for strike price : {i} is {token_row.item()}")

# a = getTokenValue(df=token_df, CE_PE='CE', strike_price=46500)
# print(f"Token is {a.item()}")
