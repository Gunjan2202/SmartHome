#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask, redirect, url_for, request,jsonify
from flask import Flask, request, render_template
import re
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import nltk
import re
from random import randint
import libnum
import sys


p=61 #CONSTANT
q=67 #CONSTANT
n = p*q

def Pallier_add(a,b):
    #converts a+b to a*b mod n
    global n
    return ((a%(n*n))*(b%(n*n)))%(n*n)
def Pallier_mul(k,a):
    #converts k*a to a^k mod n
    global n
    return (pow(int(a),int(k),n*n)*(pow(int(a),int(k))%(n*n)))%(n*n)

def weightloader():
    weights=[]
    f=open("essentials/deathblowv2.txt","r")
    count=0
    for line in f:
        count+=1
        indu=line.split(",")

        curar=[]
        for i in indu:
            if(i !='\n'):
                curar.append(float(i))
        weights.append(curar)
    
    return weights
print("CyHome's Admin Package successfully imported")

