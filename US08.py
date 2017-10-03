#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:26:52 2017

@author: Harish7KJ
"""

from datetime import datetime
import csv

def US_08():
    with open("families.csv","r+") as fp:
        family_id = []
        indi_id = []
        marriage_dates = []
       
        for line in fp.readlines():
            lineS = line.split(',')
            family_id.append(lineS[0])
            indi_id.append(lineS[7])
            marriage_dates.append((lineS[1]))
        
    family_id = family_id[1:]
    indi_id = indi_id[1:]
    marriage_dates= marriage_dates[1:]
    family_to_indv = dict(zip(family_id, indi_id))
    familt_to_marriage = dict(zip(family_id,marriage_dates))
   

    id_to_birthdates = {}
    with open('individuals.csv','r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_indv.values():
                if lineS[0] in i:
                    id_to_birthdates[lineS[0]]= lineS[3]

    mardate = []
    bday = []
    for k,v in family_to_indv.items():
        if familt_to_marriage.get(k) != 'NA':
            for l,m in id_to_birthdates.items():
                if l in v:
                    bday = m
                    mardate = familt_to_marriage.get(k)
                    if(datetime.strptime(bday, '%d %b %Y') < datetime.strptime(mardate, '%d %b %Y')) :
                            print('ERROR: INDIVIDUAL: US08: ' + l +
                              ': Child Birth ' + bday + ' before parents ' + k +
                              ' marriage ' + mardate)
                    
                    
                        
(US_08())                       