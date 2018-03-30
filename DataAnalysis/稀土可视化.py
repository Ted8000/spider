import matplotlib.pyplot as plt
import pymongo
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

client = pymongo.MongoClient('localhost', 27017)
db = client.teddata
collection = db.allxitu

name = set()
for i in collection.find():
    name.add(i['Name'])
name = list(name)
for t in range(len(name)):
    price = []
    time = []
    for i in collection.find({'Name': '{}'.format(name[t])}).sort("Time"):
        price.append(i['MeanPrice'])
        time.append(i['Time'][2:])
    x = np.linspace(2015, 2018, collection.find({'Name': '{}'.format(name[t])}).count())
    y = np.array(price)

    plt.subplot(111)
    plt.plot(x, y, '-')
    plt.ylabel(collection.find({'Name':'{}'.format(name[t])})[0]['Unit_price'])
    plt.title('a table of {}价格'.format(name[t]))
    plt.savefig('{}.png'.format(name[t]))
    plt.close()
    # plt.show()