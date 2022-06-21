import sqlite3

import matplotlib.pyplot as plt
import numpy as np
from windrose import WindroseAxes

my_dict = {"Західний":180, "Південний": 270, "Змінний":0, "Північний":90,
           "Східний":0, "Пд-Зх":225, "Пд-Сх":315, "Пн-Зх":135,"Пн-Сх":45, "Штиль":0}


def format_data(date_1, date_2):
    date_1="'"+date_1+"'"
    date_2="'"+date_2+"'"
    return date_1, date_2


def autolabel(rects, labels=None,  height_factor=1.01):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if labels is not None:
            try:
                label = labels[i]
            except (TypeError, KeyError):
                label = ' '
        else:
            label = '%d' % int(height)
        plt.gca().text(rect.get_x() + rect.get_width()/2., height_factor*height,
                '{}'.format(label),
                ha='center', va='bottom')


def graphics_2(city, date_1, date_2):
    date_1, date_2 = format_data(date_1, date_2)
    sql = "SELECT T, count(*) FROM data_{:} WHERE date_time>={:} and date_time<={:} GROUP BY T ORDER BY T ;".format(city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    s = np.array(s)
    plt.title('Тривалість температурних режимів')
    plt.xlabel('Температура, С')
    plt.ylabel('Час, год')
    plt.bar(s[:, 0], s[:, 1]/4, color='green')
    plt.xticks(np.arange(min(s[:, 0]), max(s[:,0])+1, step=1))

    ax = plt.gca()
    autolabel(ax.patches, s[:,1] / 4, height_factor=1.01)
    # plt.show()
    plt.savefig("static/wea/img/demo_2.png")
    plt.gcf().clear()
    # print(s)
    return s


def graphics_4(city, date_1, date_2):
    date_1, date_2 = format_data(date_1, date_2)
    sql = "SELECT FF, count(*) FROM data_{:} WHERE date_time>={:} and date_time<={:} GROUP BY FF ORDER BY FF;".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    s = np.array(s)

    plt.title('Тривалість режимів вітрової активності')
    plt.xlabel('Швидкість, м/с')
    plt.ylabel('Час, год')
    plt.xticks(np.arange(min(s[:, 0]), max(s[:, 0])+1, step=1))
    ax=plt.gca()
    ax.grid(axis='y')
    ax.bar(s[:, 0], s[:, 1]/4)
    plt.savefig('static/wea/img/demo_4.png')
    plt.gcf().clear()
    # print(s[1][0])
    return s


def graphics_1(city, date_1, date_2):
    date_1, date_2 = format_data(date_1, date_2)
    sql = "SELECT T, date_time FROM data_{:} WHERE date_time>={:} and date_time<={:} ORDER BY date_time;".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    data = np.array(s)
    fig = plt.figure(figsize=(7.5, 10.5))
    plt.title('Температурні умови регіону')
    plt.xlabel('Дата і час')
    plt.ylabel('Температура, С')
    plt.grid(True)
    plt.plot(data[:, 1], data[:,0].astype(int))
    step = 1
    if len(data[:,1])>240:
        step = 48
    elif len(data[:,1])>144:
        step=24
    elif len(data[:,1])>40:
        step = 12

    plt.xticks(np.arange(0, len(data[:,1])/2+step, step=step), rotation=45)
    plt.width=len(data[:,1])
    plt.savefig("static/wea/img/demo_1.png")
    plt.gcf().clear()
    return s


def graphics_3(city, date_1, date_2):
    date_1, date_2 = format_data(date_1, date_2)
    sql = "SELECT FF, dd FROM data_{:} WHERE date_time>={:} and date_time<={:};".format(
        city, date_1, date_2)
    connector = sqlite3.connect("db.sqlite3")
    s = connector.execute(sql).fetchall()
    ax = WindroseAxes.from_ax()
    data_t = []
    data_c=[]
    plt.title('Троянда вітрів')
    for s_1 in s:
        data_t.append(s_1[0])
        data_c.append(my_dict[s_1[1]])

    ax.bar(data_c, data_t, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.savefig("static/wea/img/demo_3.png")
    plt.gcf().clear()
    return s

#
# graphics_2("kyiv", "2012-01-01 00:00", "2012-01-01 23:59")
# graphics_1("kyiv", "2012-01-01 00:00", "2012-01-01 23:59")
# graphics_3("kyiv", "2012-01-01 00:00", "2012-01-04 23:59")
# graphics_4("kyiv", "2012-01-01 00:00", "2012-01-01 23:59")





