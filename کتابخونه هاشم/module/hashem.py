      
import datetime
import time
import pandas as pd
import MetaTrader5 as mt5
import statistics



# Total positions
def total_positons():
    positions_total=mt5.positions_total()
    return positions_total


# balance
def balance():
    balance = mt5.account_info()._asdict()['balance']
    return balance


# profit
def profit():
    positions = mt5.positions_get()
    profit = 0
    for position in positions:
        profit += position._asdict()['profit']
    return profit

# kandel
def kandel(timeframe='30m', limit=10 , symbol = 'BTCUSD.'):
       
    symbol = symbol
    if timeframe == '5m':
        time = mt5.TIMEFRAME_M5
    if timeframe == '3m':
        time = mt5.TIMEFRAME_M3
    if timeframe == '1m':
        time = mt5.TIMEFRAME_M1
    if timeframe == '15m':
        time = mt5.TIMEFRAME_M15
    if timeframe == '30m':
        time = mt5.TIMEFRAME_M30
    if timeframe == '1h':
        time = mt5.TIMEFRAME_H1
    if timeframe == '4h':
        time = mt5.TIMEFRAME_H4
    if timeframe == '1d':
        time = mt5.TIMEFRAME_D1
    if timeframe == '1w':
        time = mt5.TIMEFRAME_W1
    candles = mt5.copy_rates_from_pos(symbol, time, 0, limit)
    df = pd.DataFrame(candles, columns=['time', 'open', 'high', 'low', 'close'])
    return df.iloc

# rsi
def rsi(timeframe = '15m' , symbol = 'BTCUSD.'):
            
    ohlc = kandel(timeframe, limit=50 , symbol = symbol)
    if timeframe == "1h" :
        kandle = 10
    elif timeframe == "4h" :
        kandle = 8
    elif timeframe == "1d" :
        kandle = 10
    elif timeframe == "1w" :
        kandle = 10
    elif timeframe == "30m" :
        kandle = 10
    elif timeframe == "15m" :
        kandle = 15
    elif timeframe == "5m" :
        kandle = 14
    elif timeframe == "3m" :
        kandle = 14
    elif timeframe == "1m" :
        kandle = 14
    profit = []
    loss = []
    i = -1
    for n in range(50) :
        
        if ohlc[i]['open'] > ohlc[i]['close']:
            if len(loss) < kandle :
                loss.append((ohlc[i]['open']) - (ohlc[i]['close']) )
        else:
            if len(profit) < kandle :
                profit.append(ohlc[i]['close'] - ohlc[i]['open'])
        i -= 1
    
    profitAvg = statistics.mean(profit)
    lossAvg = statistics.mean(loss)
    RS = profitAvg/lossAvg
    RSI = 100 - (100 / (1 + RS))
    return RSI


# lot
def qty(myBalance):
    if myBalance < 300:
        lot =  0.01
        return lot
    elif myBalance >= 300 and myBalance <= 499:
        lot =  0.02
        return lot
    elif myBalance >= 500 and myBalance <= 999:
        lot = 0.03
        return lot
    elif myBalance >= 1000 and myBalance <= 1499:
        lot = 0.04
        return lot
    elif myBalance >= 1500 and myBalance <= 1999:
        lot = 0.05
        return lot
    elif myBalance >= 2000 and myBalance <= 2499:
        lot = 0.06
        return lot
    elif myBalance >= 2500 and myBalance <= 2999:
        lot = 0.07
        return lot
    elif myBalance >= 3000 and myBalance <= 3999:
        lot = 0.08
        return lot
    elif myBalance >= 4000 and myBalance <= 5000:
        lot = 0.09
        return lot
    elif myBalance > 5000:
        lot = 0.1
        return lot
    

# create_order
def create_order(symbol , lot , order_type , price , sl , tp , comment):
    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl" : sl,
        "tp" : tp,
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
        }
    order = mt5.order_send(request)
    return order


#close_order
def close_order(symbol , lot , order_type , price , ticket):
    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "position": ticket,
        "price": price,
        "comment": "close by hashem",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    return result



# moving average 26
def average26(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=26 , symbol = symbol)
    average = statistics.mean(item['low'] for item in ohlc)
    return average


# moving average 12
def average12(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=12 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average


# moving average 50
def average50(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=50 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average


# moving average 60
def average60(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=60 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average


# moving average 162
def average162(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=162 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average


# moving average 100
def average100(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=100 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average



# moving average 200
def average200(timeframe , symbol ='BTCUSD.'):
        
    ohlc = kandel(timeframe , limit=200 , symbol = symbol)
    average = statistics.mean(item['close'] for item in ohlc)
    return average


# long or short
def whatKandel(timeframe = '30m' , candle = -1 , symbol ='BTCUSD.'):
    ohlc = kandel(timeframe , limit=10 , symbol = symbol)
    if ohlc[candle]['open'] > ohlc[candle]['close']:
        return 'short'
    else:
        return 'long'
    


def isBeta(timeframe , candel , symbol ='BTCUSD.' , m = 50):
    kandels = kandel(timeframe , limit=10 , symbol = symbol)
    res = kandels[candel]
    if res['open'] > res['close']:
        # short kandel
        if res['open'] == res['high'] and (res['close'] - res['low']) <= res['open'] - res['close'] and body(timeframe , candel ,symbol ) >= m :
            return True
        else:
            return False
    elif res['open'] < res['close']:
        # long kandel
        if res['open'] == res['low']  and (res['high'] - res['close']) <= res['close'] - res['open'] and body(timeframe , candel ,symbol ) >= m :
            return True
        else:
            return False
    else:
        return False
    



def isBack(timeframe , candel , upOrDown , symbol ='BTCUSD.'):
    kandels = kandel(timeframe , limit=10 , symbol = symbol)
    res = kandels[candel]
    if res['open'] > res['close']:
        # short kandel
        if upOrDown == 'up'and (res['open'] - res['close'])*3 < res['high'] - res['open'] and (res['close'] - res['low']) * 3 <= res['high'] - res['open'] :
            return True
        
        elif upOrDown == 'down'and (res['open'] - res['close'])*4 < res['close'] - res['low'] and (res['high'] - res['open'])*3 <= res['close'] - res['low'] :
            return True
        else:
            return False
        
    elif res['open'] < res['close']:
        # long kandel
        if upOrDown == 'up'and (res['close'] - res['open'])*4 < res['high'] - res['close'] and res['high'] - res['close'] > (res['open'] - res['low'])*3 :
            return True
        
        elif upOrDown == 'down'and (res['close'] - res['open'])*3 < res['open'] - res['low'] and (res['high'] - res['close'])*3 < res['open'] - res['low']:
            return True
        
        else:
            return False
    else:
        return False



def body(timeframe , candel , symbol ='BTCUSD.'):
    kandels = kandel(timeframe , limit=10 , symbol = symbol)
    res = kandels[candel]
    if res['open'] > res['close']:
        # short kandel
        body = res['open'] - res['close']
        return body
        
    elif res['open'] < res['close']:
        # long kandel
        body = res['close'] - res['open']
        return body
    else:
        return 0
    


def check_time(start_hour, end_hour):
    current_time = datetime.datetime.now(datetime.UTC).time()
    if current_time.hour >= start_hour and current_time.hour <= end_hour:
        return True
    else:
        return False
    

def hemayat(symbol):
    kandeld = kandel('1d' , 5 , symbol )
    kandelw = kandel('1w' , 5 , symbol )
    kande4h = kandel('4h' , 5 , symbol )
    kande1h = kandel('1h' , 5 , symbol )
    lines = [kandeld[-2]['high'] , kandeld[-2]['low'] , kandelw[-1]['high'] , kandelw[-1]['low'] , kandelw[-2]['high'] , kandelw[-2]['low'] , kande4h[-2]['high'] , kande4h[-2]['low'] , kande1h[-2]['high'] , kande1h[-2]['low']]
    price = mt5.symbol_info_tick(symbol).ask
    line = []
    for i in lines:
        if i < price:
            line.append(i)
    if len(line) == 0:
        return False
    else:
        return max(line)
        

def moghavemat(symbol):
    kandeld = kandel('1d' , 5 , symbol )
    kandelw = kandel('1w' , 5 , symbol )
    kande4h = kandel('4h' , 5 , symbol )
    kande1h = kandel('1h' , 5 , symbol )
    lines = [kandeld[-2]['high'] , kandeld[-2]['low'] , kandelw[-1]['high'] , kandelw[-1]['low'] , kandelw[-2]['high'] , kandelw[-2]['low'] , kande4h[-2]['high'] , kande4h[-2]['low'] , kande1h[-2]['high'] , kande1h[-2]['low']]
    price = mt5.symbol_info_tick(symbol).ask
    line = []
    for i in lines:
        if i > price:
            line.append(i)
    if len(line) == 0:
        return False
    else:
        return min(line)
        


def kijun_sen(symbol ,timeframe ,num):
    kandels = kandel(timeframe =timeframe , limit=num , symbol = symbol)
    high = []
    low = []
    i = -1
    for n in range(num) :
        high.append(kandels[i]['high'])
        low.append(kandels[i]['low'])
        i -= 1
    mini = min(low)
    maxi = max(high)
    sen = (maxi + mini ) / 2 
    return sen



def kijun_sen_befor(symbol ,timeframe ,num):
    x = num + 2
    kandels = kandel(timeframe =timeframe , limit=x , symbol = symbol)
    high = []
    low = []
    i = -3
    for n in range(num) :
        high.append(kandels[i]['high'])
        low.append(kandels[i]['low'])
        i -= 1
    mini = min(low)
    maxi = max(high)
    sen = (maxi + mini ) / 2 
    return sen



def ema20(timeframe,symbol):
    prices = []
    ohlc = kandel(timeframe , limit=20 , symbol = symbol)
    i = -1
    for n in range(20) :
        prices.append((ohlc[i]['close']) )
        i -= 1

    if len(prices) < 20:
        return False
    
    sma = sum(prices[:20]) / 20
    
    k = 2 / (20 + 1)

    ema = sma

    for price in prices[20:]:
        ema = (price - ema) * k + ema
    
    return ema

def ema50(timeframe,symbol):
    prices = []
    ohlc = kandel(timeframe , limit=50 , symbol = symbol)
    i = -1
    for n in range(50) :
        prices.append((ohlc[i]['close']) )
        i -= 1

    if len(prices) < 50:
        return False
    
    sma = sum(prices[:50]) / 50
    
    k = 2 / (50 + 1)

    ema = sma

    for price in prices[50:]:
        ema = (price - ema) * k + ema
    
    return ema

def ema100(timeframe,symbol):
    prices = []
    ohlc = kandel(timeframe , limit=100 , symbol = symbol)
    i = -1
    for n in range(100) :
        prices.append((ohlc[i]['close']) )
        i -= 1

    if len(prices) < 100:
        return False
    
    sma = sum(prices[:100]) / 100
    
    k = 2 / (100 + 1)

    ema = sma

    for price in prices[100:]:
        ema = (price - ema) * k + ema
    
    return ema

def ema200(timeframe,symbol):
    prices = []
    ohlc = kandel(timeframe , limit=200 , symbol = symbol)
    i = -1
    for n in range(200) :
        prices.append((ohlc[i]['close']) )
        i -= 1

    if len(prices) < 200:
        return False
    
    sma = sum(prices[:200]) / 200
    
    k = 2 / (200 + 1)

    ema = sma

    for price in prices[200:]:
        ema = (price - ema) * k + ema
    
    return ema

def ema(timeframe, window , symbol):
    prices = []
    ohlc = kandel(timeframe , limit=window , symbol = symbol)
    i = -1
    for n in range(window) :
        prices.append((ohlc[i]['close']) )
        i -= 1

    if len(prices) < window:
        return False
    
    sma = sum(prices[:window]) / window
    
    k = 2 / (window + 1)

    ema = sma

    for price in prices[window:]:
        ema = (price - ema) * k + ema
    
    return ema



tokyo = check_time(0 , 8)
londen = check_time(7 , 15)
new_york = check_time(13 , 19)
sydney = check_time(22 , 5)


buy = mt5.ORDER_TYPE_BUY
sell = mt5.ORDER_TYPE_SELL
