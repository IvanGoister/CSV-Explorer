#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import csv
import sys
import InfoInRow

results=[]
#File=('2014DB.csv')
with open('2014DB.csv') as Base:
    a=0
    reader=csv.DictReader(Base,  delimiter=';')
    for row in reader:
        InfoInRow.info(row)
        #results.append(row)
        a=a+1


        





