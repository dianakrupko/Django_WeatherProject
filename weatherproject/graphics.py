import sqlite3

import matplotlib.pyplot as plt
import numpy as np
from windrose import WindroseAxes


my_dict = {"Західний":180, "Південний": 270, "Змінний":0, "Північний":90,
           "Східний":0, "Пд-Зх":225, "Пд-Сх":315, "Пн-Зх":135,"Пн-Сх":45, "Штиль":0}
def graphics_2(city, date_1, date_2):
    sql = "SELECT T, count(*) FROM data_{:} WHERE date_time>={:} and date_time<={:} GROUP BY T ORDER BY T ;".format(city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    s = np.array(s)
    data_t = []
    data_c = []
    # print(s)
    # data=0
    # for s_1 in s:
    #     data_t.append(s_1[0])
    #     data_c.append(s_1[1]/2)
    #     data += s_1[1]/2
    # print(data)
    plt.bar(s[:, 0], s[:, 1]/2)
    plt.show()


def graphics_4(city, date_1, date_2):
    sql = "SELECT FF, count(*) FROM data_{:} WHERE date_time>={:} and date_time<={:} GROUP BY FF ORDER BY FF;".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    s = np.array(s)
    data_t = []
    data_c = []
    print(s)

    plt.bar(s[:, 0], s[:, 1]/2)
    plt.show()


def graphics_1(city, date_1, date_2):
    sql = "SELECT T, date_time FROM data_{:} WHERE date_time>={:} and date_time<={:} ORDER BY date_time;".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    data = np.array(s)

    # plt.scatter( data[:, 1], data[:,0])
    # plt.show()
    print(data[:, 1])
    plt.plot(data[:, 1], data[:,0])
    plt.show()


def graphics_3(city, date_1, date_2):
    sql = "SELECT FF, dd FROM data_{:} WHERE date_time>={:} and date_time<={:};".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()

    data = np.array(s)
    # print(s)
    # for d in data:
    #     d[1]=int(my_dict[d[1]])
    # print(data)
    print(data[:,1])
    ws = np.random.random(96) * 6
    wd = np.random.random(500) * 360
    ax = WindroseAxes.from_ax()
    print(len(data[:,1]))
    data_t = []
    data_c=[]
    for s_1 in s:
        data_t.append(s_1[0])
        data_c.append(my_dict[s_1[1]])

    ax.bar(data_c, data_t, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.savefig("demo.png")

# graphics_2("kyiv", "'2012-01-01 00:00'", "'2012-01-01 23:59'")
# graphics_4("kyiv", "'2012-01-01 00:00'", "'2012-01-01 23:59'")
# graphics_1("kyiv", "'2012-01-01 00:00'", "'2012-01-01 23:59'")
graphics_3("kyiv", "'2012-01-01 00:00'", "'2012-01-04 23:59'")






