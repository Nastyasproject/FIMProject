import os
import pandas as pd
import numpy as np
from openpyxl import Workbook 

def sort(path):#path - адрес к таблице

# Считываем xlsx-файл -> 'my_book.xlsx' - тут полный путь к файлу
  df = pd.read_excel(path)

# сортировка по столбцу 'id'
  df.sort_values(by=['id'], inplace=True)



def update(path , save):
  df = pd.read_excel(path)
  if(path=='Хранилище/1.xlsx'):
    df['id'] = df['id'] - 7420
  if(path=='Хранилище/2.xlsx'):
    df['id'] = df['id'] - 7851
  if(path=='Хранилище/3.xlsx'):
    df['id'] = df['id'] - 8573
  df.to_excel(path)
  dfFinal = df
  print(dfFinal)

