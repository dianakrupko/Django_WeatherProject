import sqlite3

import pandas as pd
from pandas import isnull

pd.options.mode.chained_assignment = None
my_dict = {"Западный": "Західний", "Южный": "Південний", "Переменный": "Змінний", "Северный": "Північний", "Восточный": "Східний"}


class Data:

    def __init__(self, name_file, name_db):
        self.name_file = name_file
        self.table = pd.read_excel(self.name_file)
        self.table_rows = self.table.shape[0]
        self.connector = sqlite3.connect(name_db)
        self.cursor = self.connector.cursor()

    def edit_data(self, name_method):
        self.table['Число месяца'] = self.table['Число месяца'].interpolate(method=name_method)
        self.table['FF'] = self.table['FF'].interpolate(method=name_method)
        self.table['T'] = self.table['T'].interpolate(method=name_method)
        for i in range(self.table_rows):
            if not isnull(self.table['dd'][i]) and len(self.table['dd'][i]) > 3:
                self.table['dd'][i] = my_dict[self.table['dd'][i]]
            if isnull(self.table['dd'][i]) and self.table['FF'][i] == 0:
                self.table['dd'][i] = "Штиль"
        self.table['dd'].fillna(method="pad", inplace=True)
        self.table['UTC'] = self.table['UTC'].interpolate(method=name_method)
        for i in range(self.table_rows):
            self.table['UTC'][i] = self.func(float(self.table['UTC'][i]))

    def func(self, time: float):
        time = time*24
        minutes = time % 1
        if minutes:
            min = "30"
        else:
            min = "00"
        txt = "{hours:0>2}:{min}".format(hours=int(time // 1), min=min)
        return txt

    def my_db(self):
        for i in range(self.table_rows):
            sql = "INSERT INTO Lviv (Date, T, dd, F) VALUES (?, ?, ?, ?);"
            txt = self.name_file[20:27]
            txt += "-"
            txt += "{:0>2} ".format(self.table['Число месяца'][i])
            txt += self.table['UTC'][i]
            # print(txt)
            self.connector.execute(sql, (txt, int(self.table['T'][i]), self.table['dd'][i], int(self.table['FF'][i])))
        self.connector.commit()


def delete_table(name_db):
    sql = "DELETE FROM Lviv;"
    connector = sqlite3.connect(name_db)
    connector.execute(sql)
    connector.commit()


# def edit(name_inter):
#     for i in range(12):
#         txt = "static/main/my_data/2012-{:0>2}.xlsx".format(i+1)
#         # txt = "static\main\my_data\\2012-{:0>2}.xlsx".format(i+1)
#         print(txt)
#         data = Data(txt, "db.sqlite3")
#         data.edit_data(name_inter)
#         print(546456)
#         data.my_db()


# data1 = Data("static/main/my_data/2012-01.xlsx", "db.sqlite3")
# data1.edit_data("linear")
# data1.my_db()
# delete_table("db.sqlite3")
# edit("linear")
