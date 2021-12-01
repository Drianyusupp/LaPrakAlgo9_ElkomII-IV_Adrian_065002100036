# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:22:48 2021

@author: User
"""

print("====== PROGRAM MENGHITUNG RATA-RATA VALUE ======")

print("Tuple 1 : ")

angka = (21,10,8,20,23,24,26,15,30,12,18,56,67,34,27,31)
tuple1 = (angka[0:4])
tuple2 = (angka[4:8])
tuple3 = (angka[8:12])
tuple4 = (angka[12:16])
print((tuple1,tuple2,tuple3,tuple4))

print("Rata-rata nilai pada masing-masing tuple adalah : ")
print([sum(tuple1)/float(len(tuple1)),sum(tuple2)/float(len(tuple2)),sum(tuple3)/float(len(tuple3)),sum(tuple4)/float(len(tuple4))])