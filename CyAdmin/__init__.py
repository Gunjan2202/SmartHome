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
import numpy as np
import tensorflow as tf
import nltk
import re
import keras
from keras import models
from keras import layers
from keras import optimizers
from random import randint
import libnum
import sys


p=61 #CONSTANT
q=67 #CONSTANT
n = p*q

def Pallier_add(a,b):
    global n
    return ((a%(n*n))*(b%(n*n)))%(n*n)
def Pallier_mul(k,a):
    global n
    return (pow(a,int(k),n*n)*(int(pow(a,k-int(k)))%(n*n)))%(n*n)

def weightloader():
    weights=[]
    f=open("essentials/taskbeast.txt","r")
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

