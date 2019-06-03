#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import csv
import sys

results=[]
#File=('2014DB.csv')
with open('2014DB.csv') as Base:
    a=0
    
    reader=csv.DictReader(Base,  delimiter=';')
    for row in reader:
        if a < 2:
            print("ROW it's ", type(row))
            #print(row)
            print "Тип кузова - ", row['body']
            print "Категорія - ", row['kind']
            print "Об'єм двигуна - ", row['capacity']
            print 'Спорядженна маса - ', row['own_weight']
            print 'Торгова назва - ', row['brand']
            print 'Рік випуску - ', row['make_year']
            print 'Повна маса - ', row['total_weight']
            print 'Дата реєстрації - ', row['d_reg']
            print 'Назва операції - ', row['oper_name']
            print 'Персон - ', row['person']
            print 'Паливо - ', row['fuel']
            print 'Модель - ', row['model']
            print 'Реєстраційний номер - ', row['n_reg_new']
            print 'Колір - ', row['color']
            print 'Призначення - ', row['purpose']
            results.append(row)
        a=a+1


        


