import backtrader as bt

data = bt.feeds.IBData(dataname='EUR.USD-CASH-IDEALPRO',
                       host='127.0.0.1', port=7496, clientId=35)

print(data)
