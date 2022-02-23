import sqlite3

import pandas as pd
from pandas import isnull

pd.options.mode.chained_assignment = None
my_dict = {"Западный": "Західний", "Южный": "Південний", "Переменный": "Змінний", "Северный": "Північний",
           "Восточный": "Східний", "Ю-З": "Пд-Зх", "Ю-В": "Пд-Сх", "С-З": "Пн-Зх","С-В":"Пн-Сх"}

cities = ["lviv", "kyiv", "ivano_frankivsk", "dnipropetrovsk", "donetsk", "krivoy_rog", "luhansk", "odessa", "kharkiv",
          "simferopol"]


class Data:

    def __init__(self, name_file, name_db):
        self.name_file = name_file
        self.table = pd.read_excel(self.name_file)
        self.table_rows = self.table.shape[0]
        self.connector = sqlite3.connect(name_db)
        self.cursor = self.connector.cursor()

    def edit_data(self, name_method):
        self.table['Число месяца'] = self.table['Число месяца'].interpolate(method=name_method, order=1)
        self.table['FF'] = self.table['FF'].interpolate(method=name_method, order=1)
        self.table['T'] = self.table['T'].interpolate(method=name_method, order=1)
        for i in range(self.table_rows):
            if not isnull(self.table['dd'][i]):
                self.table['dd'][i] = my_dict[self.table['dd'][i]]
            if isnull(self.table['dd'][i]) and self.table['FF'][i] == 0:
                self.table['dd'][i] = "Штиль"
        self.table['dd'].fillna(method="pad", inplace=True)
        self.table['UTC'] = self.table['UTC'].interpolate(method=name_method, order=1)
        # print(self.table['UTC'][0])
        # for i in range(self.table_rows):
        #     self.table['UTC'][i] = self.func(float(self.table['UTC'][i]))
        # print(self.table['UTC'][i])

    def func(self, time: float):
        time = time * 24
        minutes = time % 1
        if minutes:
            min = "30"
        else:
            min = "00"
        txt = "{hours:0>2}:{min}".format(hours=int(time // 1), min=min)
        return txt

    def my_db(self, city):
        for i in range(self.table_rows - 1):
            sql = "INSERT INTO data_{:} (date_time, T, dd, FF) VALUES (?, ?, ?, ?);".format(city)
            txt = self.lala()
            txt += "-"
            txt += "{:0>2} ".format(self.table['Число месяца'][i])
            txt += self.func(float(self.table['UTC'][i]))
            # print(txt)
            # print(self.table['UTC'][i])
            self.connector.execute(sql, (txt, int(self.table['T'][i]), self.table['dd'][i], int(self.table['FF'][i])))
        self.connector.commit()

    def lala(self):
        ind1 = 100
        txt = ""
        ind2 = 100
        for i in range(len(self.name_file)):
            if self.name_file[i] == '/' and self.name_file[i - 1] != 's':
                ind1 = i
            if self.name_file[i] == '.':
                ind2 = i
            if ind1 < i < ind2:
                txt += self.name_file[i]
        return txt


def delete_table(name_db):
    connector = sqlite3.connect(name_db)
    for city in cities:
        sql = "DELETE FROM data_{:};".format(city)
        print(sql)
        connector.execute(sql)
    connector.commit()


def edit(name_inter):
    # cities = ["lviv", "Kyiv", "Ivano_Frankivsk", "Dnipropetrovsk","Donetsk","Krivoy_rog", "Luhansk", "Odessa", "Kharkiv"]
    for city in cities:
        for i in range(12):
            txt = "datas/{:}/2012-{:0>2}.xlsx".format(city, i + 1)
            print(txt)
            data = Data(txt, "db.sqlite3")
            data.edit_data(name_inter)
            print(546456)
            data.my_db(city)


def search(name_db, string, city):
    sql = "SELECT * FROM data_{:} WHERE date_time LIKE '{:}%';".format(city, string)
    print(sql)
    connector = sqlite3.connect(name_db)
    s = connector.execute(sql).fetchall()
    return s

# data1 = Data("datas/lviv/2012-01.xlsx", "db.sqlite3")
# print(data1.lala("lviv"))
# data1.edit_data("linear")
# data1.my_db("lviv")
# delete_table("db.sqlite3")
# edit("polynomial")
# search("db.sqlite3", "2012-02")
