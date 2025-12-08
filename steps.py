# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:33:58 2023

@author: KD
"""
import matplotlib.pyplot as plt

#lista dni w poszczególnych miesiącach
month_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Czer', 'Lip', 'Sier', 'Wrz', 'Paź', 'List', 'Gru']
steps_month = []
s = 0

with open('steps.txt') as f:
    #odczyt z pliku i tworzenie listy sumy kroków w poszczególnych miesiącach
    for m in month_d:
        for i in range(m):
            s += int(f.readline())
        steps_month.append(s)
        s = 0

#wykres sumy kroków w poszczególnych miesiącach
plt.bar(month, steps_month)
plt.title('Suma kroków w poszczególnych miesiącach')

#obliczenie redniej kroków w poszczególnych miesiącach
plt.figure()
steps_month = [steps_month[i] / month_d[i] for i in range(12)]
plt.bar(month, steps_month)
plt.title('Średnia kroków w poszczególnych miesiącach')
