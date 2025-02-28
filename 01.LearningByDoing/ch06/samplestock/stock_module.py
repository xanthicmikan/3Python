import requests
import twstock


def get_setting():
    try:
        with open('stock.txt') as f:
            slist = f.readlines()
            res = []
            for lst in slist:
                s = lst.split(',')
                res.append([s[0], float(s[1]), float(s[2])])
    except:
        print('stock.txt 讀取錯誤')
        return None
    return res


def get_price(stockid):
    #rt = twstock.realtime.get(stockid) 
    rt = {'info':{'name':'0056'}, 'realtime':{'latest_trade_price':'160'}, 'success':True}#sample data for testing
    if rt['success']:
        return (rt['info']['name'],
                float(rt['realtime']['latest_trade_price']))
    else:
        return (False, False)


def get_best(stockid):
    #stock = twstock.Stock(stockid)#sample data for testing
    stock = [140.2, 140.6, 147.6, 149, 140.1, 145.5]
    #bp = twstock.BestFourPoint(stock).best_four_point()#sample data for testing
    bp = (True, '量大收紅,三日均價>六日均價')
    if(bp):
        return ('Buy' if bp[0] else 'Sell', bp[1])
    else:
        return (False, False)

