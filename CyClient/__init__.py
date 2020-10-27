from flask import Flask, redirect, url_for, request,jsonify
from flask import Flask, request, render_template
import re
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import requests
import nltk
import re
from random import randint
import libnum
import webbrowser
import sys

#######   step 1   #######
p=61 #CONSTANT
q=67 #CONSTANT , both constant should be independent of each other
n = p*q



#function definition
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def  lcm(a, b):
    return a * b // gcd(a, b)

def L(x,n):
    return ((x-1)//n)

#condition checking
if (p==q):
    print("P and Q cannot be the same")
    

if (gcd(p*q,(p-1)*(q-1))==1):
    print("P and Q are not independent of each other")
    

########   step 2   #############
gLambda = lcm(p-1,q-1)

########   step 3   #############
g=2 #select any random integer
r=1 


########   step 4   #############
l = (pow(g, gLambda, n*n)-1)//n
gMu = libnum.invmod(l, n)
'''
if (gcd(g,n*n)==1):
    print("g is relatively prime to n*n")
else:
    print("WARNING: g is NOT relatively prime to n*n. Will not work!!!")


ONLY MAKE CHANGES AFTER THIS LINE. ALL CONSTANTS AND FUNCTIONS SPECIFIED ABOVE NEED NOT BE ALTERED

'''
# print("Public key : \n")
# print(" ".join([n,g]))

# print("Private key : \n")
# print(" ".join([gLambda,gMu]))


def Pallier_encrpyt(m):    #THE MESSAGE-NUMBER TO BE ENCRYPTED

    #MESSAGE ENCRYPTION: converting m variable to cipher variable
    r=randint(1,n)
    if(r%p==0):
        r-=1
    if(r%q==0):
        r-=1
    k1 = (pow(g, int(m), n*n))%(n*n)
    k2 = pow(r, n, n*n)
    cipher = ((k1% (n*n))*(k2% (n*n)))%(n*n)
    return cipher

def Pallier_decrpyt(cipher):    #THE MESSAGE-NUMBER TO BE ENCRYPTED

    #MESSAGE DECRYPTION: converting cipher variable to message variable
    l = (pow(cipher, gLambda, n*n)-1) // n
    message= ((l%n) * (gMu%n)) % n
    return message


'''
Driver code: just to see if things are working properly lol

m=2
cipher=Pallier_encrpyt(m)
message=Pallier_decrpyt(cipher)


print("p=",p,"\tq=",q)
print("g=",g,"\tr=",r)
print("================================================")
print("Mu:\t\t",gMu,"||\tgLambda:\t",gLambda)
print("================================================")
print("Public key (n,g):\t\t",n,g)
print("Private key (lambda,mu):\t",gLambda,gMu)
print("\n\nFIRST NUMBER:")
print("Message:\t",m)

print("Cipher:\t\t",cipher)
print("Decrypted:\t",message)

'''
def print_keys():
    print()
    print("================================================")
    print("Public key (n,g):\t\t",n,g)
    print("Private key (lambda,mu):\t",gLambda,gMu)
    print("================================================")


def revdicto_maker():
    revdicto={}
    f=open("essentials/revdicto.txt","r")
    for line in f:
        vals=line.split(':')
        revdicto[int(vals[0])]=vals[1]
    return revdicto

preprocessing_dict={}

def aggressive_fermenter(s):
    
    global preprocessing_dict
    if(preprocessing_dict=={}):
        f=open("essentials/dicto.txt","r")
        for line in f:
            vals=line.split(':')
            preprocessing_dict[vals[0]]=int(vals[1])
        f.close()
    s=s.lower()
    stopwords=[" the"," is"," and"," get"," to"," please"]
    for stopper in stopwords:
        s=s.replace(stopper,'')
    replace_rules=[["ness",""],["you"," "],["i am"," "],["es","e"],["sses","ss"],["ies","y"],["s",""],[","," "]]


    for rule in range(len(replace_rules)):
        regstring=replace_rules[rule][0]+r"\s+"
        endreg=replace_rules[rule][0]+r"$"
        s=re.sub(regstring,replace_rules[rule][1]+" ",s)
        s=re.sub(endreg,replace_rules[rule][1]+" ",s)
        
    
    s=re.sub(r"\s\s"," ",s)
    s=re.sub(r"^\s","",s)
    s=re.sub(r"\s$","",s)
    
    vector=[0 for i in range(len(preprocessing_dict))]
    for i in preprocessing_dict.keys():

        if(s.find(i)!=-1):
            vector[preprocessing_dict[i]]=1
    
    return vector



print("CyHome's Client Package successfully imported")

