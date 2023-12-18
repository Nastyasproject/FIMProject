import pandas as pd #для обработки и анализа структурированных данных
import openpyxl #для работы с excel

from poo import sort,update


def start():
  sort('Хранилище/1.xlsx')
  update('Хранилище/1.xlsx' , '1_res.xlsx')
  sort('Хранилище/2.xlsx')
  update('Хранилище/2.xlsx' , '2_res.xlsx')
  sort('Хранилище/3.xlsx') 
  update('Хранилище/3.xlsx' , '3_res.xlsx')

if __name__ == '__main__':
  start()