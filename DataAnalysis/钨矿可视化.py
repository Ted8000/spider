import matplotlib.pyplot as plt
import pymongo
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

client = pymongo.MongoClient('localhost', 27017)
db = client.teddata
collection = db.wukuang

data = []
time = []
price = []
name = '仲钨酸铵 ≥88.5出口'
#获取均价
def getprice(price):
    a,b=price.split('-')
    return (int(a)+int(b))/2
#获取价格，按照时间排序
for i in collection.find({'name':'{}'.format(name)}).sort("time"):
    data.append(i)
    if '-' in i['price']:
        price.append(getprice(i['price']))
        time.append(i['time'])
    else:
        price.append(i['price'])
        time.append(i['time'])

# x = np.linspace(2016, 2018, collection.find({'name': '{}'.format(name)}).count())
x = [datetime.strptime(d, '%Y-%m-%d').date() for d in time]
y = np.array(price)
# 设置横坐标日期显示，interval设置间隔！！
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))

plt.subplot(111)
plt.plot(x, y, '-')
plt.ylabel(collection.find({'name': '{}'.format(name)})[0]['yuan/kg'])
plt.savefig('{}.png'.format(name))
plt.show()
plt.close()

