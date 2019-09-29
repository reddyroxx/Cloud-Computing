#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:55:22 2019

@author: rakesh
"""
'''
import random
s = "abcdefghijklmnopqrstuvwxyz"

l = [i for i in s]
alphabets = dict()

for i in range(1,27):
    alphabets[i] = l[i-1]

s = "1234567890123456789013579@"

l1 = [i for i in s]
dig = dict()

for i in range(1,27):
    dig[i] = l1[i-1]    
cat=['Petlove','Env Conservation','Humanitarian Acts','Natural Resource Conservation']
for i in range(1,301):
    a = random.randint(1,26)
    b = random.randint(1,26)
    c = random.randint(1,26)
    d = random.randint(1,26)
    e = random.randint(1,26)
    a1 = random.randint(1,26)
    b1 = random.randint(1,26)
    c1 = random.randint(1,26)
    d1 = random.randint(1,26)
    e1 = random.randint(1,26)    
    a2 = random.randint(1,26)
    b2 = random.randint(1,26)
    c2 = random.randint(1,26)
    d2 = random.randint(1,26)
    e2 = random.randint(1,26)    
    k = random.randint(0,3)
    z = random.randint(1,5000)
    v = random.randint(1,200)
    command = "INSERT INTO upload values \
       ('"+cat[k]+"',"+str(z)+",'"+(alphabets[a]+alphabets[b]+alphabets[c]+alphabets[d]+alphabets[e])+"','"+(alphabets[a1]+alphabets[b1]+alphabets[c1]+alphabets[d1]+alphabets[e1]+alphabets[a2]+alphabets[b2]+alphabets[c2]+alphabets[d2]+alphabets[e2])+"',"+str(v)+",'"+(alphabets[a]+alphabets[b]+alphabets[c2]+alphabets[d1]+alphabets[e2])+"','"+(alphabets[a1]+alphabets[b]+dig[c]+dig[c1]+alphabets[c2]+dig[d2]+alphabets[d]+alphabets[e1])+"');"
    print(command) 

'''
from flask import Flask,render_template ,redirect, url_for , request,jsonify
import sqlite3 as sql
import datetime
import hashlib
conn=sql.connect("database.db")
a="select count(act_id) from upload where category='Petlove';"
a1=list(conn.execute(a))
conn.commit()
a1=[i[0] for i in a1]
print(a1[0])

