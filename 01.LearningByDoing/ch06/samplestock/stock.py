import ssl
import time
import stock_module as m

ssl._create_default_https_context = ssl._create_unverified_context
slist = m.get_setting()
cnt = len(slist)

log1 = []
log2 = []
for i in range(cnt):
    log1.append('')
    log2.append('')

check_cnt = 20
while True:
    for i in range(cnt):
        id, low, high = slist[i]
        name, price = m.get_price(id)
        print('第', check_cnt, '次檢查：',name, '目前股價：',price, '自己預設區間：',low,'~',high)
        if price <= low:
            if log1[i] != '買進':
                log1[i]= '買進' 
        elif price >= high:
            if log1[i] != '賣出':
                log1[i]= '賣出'
        act, why = m.get_best(id)
        if why:
            if log2[i] != why:
                log2[i] = why 
    print('--------------')
    check_cnt -= 1
    if check_cnt == 0: break
    time.sleep(1)
