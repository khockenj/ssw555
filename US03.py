#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:45:47 2017

@author: Harish7KJ
"""
from datetime import datetime
import csv
def US_03():
    with open("individuals.csv", "r+") as fp:
        for line in fp.readlines():
            lineS = line.split(",")
            #print(lineS[3])
            
            if lineS[4] != "Alive" and lineS[4] != "Death":
                bday = (datetime.strptime(lineS[3], '%d %b %Y'))
                dday = datetime.strptime(lineS[4], '%d %b %Y')
                if bday>dday:  
                      print('ERROR: INDIVIDUAL: US03: ' + lineS[0] + ': Death ' + lineS[4] + ' before birth ' + lineS[3])
                   
                
(US_03())
