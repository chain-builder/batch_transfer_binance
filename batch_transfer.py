import time
from binance.client import Client
import numpy as np
import random


api_key = 'your binance api key'
secret_key = 'your secret key'
currency = 'ETH'
amount = 0.1
wait_time = 60 ## 以60s为均值。上下波动20%转账。

addresses = np.loadtxt("address.txt", dtype=str)  ###要转账钱包的地址

def randomize_data(x, randomize_type):
    random_percent = (random.random() * 0.4 - 0.2)  # 在-0.2到0.2之间随机生成一个小数
    random_value = x * random_percent  #
    y = x + random_value

    if randomize_type == "time":
        return int(y)
    else:
        return round(y, 4)

def avoid_witch_transaction(coin_type, amount, wait_time):
    client = Client(api_key, secret_key)
    amount = randomize_data(amount, "amount")  ###在-20%到20%范围内随机数据
    wait_time = randomize_data(wait_time, "time")  ###在-20%到20%范围内随机数据
    for address in addresses:
        #try:
        tx = client.withdraw(
            asset=currency,
            address=address,
            amount=amount,
            network=coin_type,
            gas_price=50  #此处以50 gwei的价格设置矿工费
        )
        time.sleep(wait_time)
        print("TxID: ", tx['id'])


avoid_witch_transaction(currency, amount, wait_time)

