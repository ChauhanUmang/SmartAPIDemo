import requests
import datetime
import pandas as pd


# Get the dataframe from smartAPI
def get_token_df():
    instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
    d = requests.get(instrument_url).json()
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry'], format='%d%b%Y').dt.date
    return token_df


def get_expiry_date():
    """
    0 - Monday
    1 - Tuesday
    2 - Wednesday
    3- Thursday
    4 for Friday
    To Calculate next Thrusday use 3, for next Friday use 4
    :return:
    """
    today = datetime.date.today()
    next_expiry = today + datetime.timedelta((3 - today.weekday()) % 7)
    return next_expiry


# Token of Equity: getTokenValue(token_df, exch_seg="NSE", name="TCS")
def get_token_value(df, expiry=get_expiry_date(), CE_PE='', strike_price=0, exch_seg='NFO',
                    name='BANKNIFTY', instrumenttype='OPTIDX'):
    """
    token_row = getTokenValue(df = token_df, CE_PE = 'CE', expiry = '27JUL2023', strike_price = 46500)
    token = token_row.item()
    :param df: dataframe of tradeable items list
    :param CE_PE: whether CE or PE
    :param expiry: expiry of the option
    :param strike_price: Strike price of the option
    :param exch_seg: exchange segment like NFO or NSE
    :param name: name of the index or STOCK like NIFTY or BANKNIFTY or TCS or INFY
    :param instrumenttype: OPTIDX or FUTIDX i.e. Option and Futures of Index
    :param instrumenttype: OPTSTK or FUTSTK i.e. Option and Futures of Stocks
    :return: token_row
    """
    if strike_price != 0:
        strike_price = format(strike_price * 100, '.6f')

    if exch_seg == 'NSE':
        token_row = df.loc[(df['exch_seg'] == exch_seg) & (df['symbol'].str.endswith('EQ')) & (df['name'] == name)]
        return token_row['token'].squeeze()
    else:
        token_row = df.loc[
            (df['exch_seg'] == exch_seg) & (df['name'] == name) & (df['instrumenttype'] == instrumenttype)
            & (df['strike'] == strike_price) & (df['expiry'] == expiry)
            & (df['symbol'].str.endswith(CE_PE))]
        return token_row['token'].squeeze()
