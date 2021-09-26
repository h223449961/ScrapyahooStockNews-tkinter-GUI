# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from ttkthemes import ThemedStyle

root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("breeze")

stock01_frame = ttk.Frame(root)
stock01_frame.pack(side=tk.TOP)
stock01_label = ttk.Label(stock01_frame, text='請輸入股票四碼')
stock01_label.pack(side=tk.LEFT)
stock01_entry = ttk.Entry(stock01_frame)
stock01_entry.pack(side=tk.LEFT)

toast01_label = ttk.Label(root)
toast01_label.pack()

def switchon01():
 df01 = pd.DataFrame(columns=["新聞標題"])
 try:
  fourname01 = str(stock01_entry.get())
  page01 = requests.get('https://ww2.money-link.com.tw/TWStock/StockNews.aspx?SymId='+fourname01+'#SubMain')
  soup01 = BeautifulSoup(page01.content, 'lxml')
  table01s = soup01.find_all('div',class_= 'NewsTitle')
  for i in table01s:
   if(i==table01s[3]):break
   s01 = pd.Series([i.find('h3').text], index=['新聞標題'])
   df01 = df01.append(s01, ignore_index=True)
   df01.index = df01.index+1
   toast01_label.configure(text = df01)
  print(df01.to_string())
 except:
  print('fault')

onbutton = ttk.Button(root, text = "開始",command = switchon01).pack()
root.mainloop()
