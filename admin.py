#!/usr/bin/env python
# coding: utf-8

# # CyHome ADMIN 
# ---
# This notebook builds a flask backend to deploy the **`taskbrain`  Deep Learning model** into a localhost server **AKA the control centre of CyHome**. 

# ## STEP 0: Prepare essentials
# 1. Import libraries
# 2. Import `taskbrain` DL model

# In[2]:


#DOWNLOAD MODEL
from CyAdmin import *

# brain=models.load_model('deathblow.h5')
weights=weightloader()
print("taskbrain is locked; weights are loaded and Ready")


# ## STEP 1: Prepare necessary HTML page responses
# 
# To check if our server is live or not, we bring up a few dummy HTML pages that test the functionality and the workflow of the Admin Server.
# 
# 

# In[3]:


docs='<!DOCTYPE html><html><h1>CyHome ADMIN is Live!</h1></html>'
print('Raw HTML ready')


# ## STEP 2: Create a Flask server with necessary request descriptions
# 
# The flask module serves as the admin centre for CyHome. It receives encrypted inputs from several clients, which are fed into the taskbrain. The resulting Output is sent back to the respective clients for further processing. 
# 

# In[9]:


app = Flask(__name__)

@app.route('/ml_encrypted',methods=["GET","POST"])
def ml_encrypted():
    global n
    if(request.method=='POST'):
        content = request.json
        processor=content['array']
        ans=[0 for x in range(len(weights))]
        print('received ML Input: ',processor)
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if(j==0):
                    ans[i]=Pallier_mul(weights[i][j],processor[j])
                else:
                    ans[i]=Pallier_add(ans[i],Pallier_mul(weights[i][j],processor[j]))
        print('\nML OP sent to client: ',ans)    
        return {'res':ans}

@app.route('/ml_normal',methods=["GET","POST"])
def ml_normal():
    global n
    
    content = request.json
    processor=content['array']
    print(processor)
    counter+=1
    ans=brain.predict(np.array([np.array(processor)]))[0]
    ans=ans.tolist()
    return {'res':ans}


# ## STEP 3: Launch the server
# **Note:** the localhost port number for ADMIN is instantiated with 51393

# In[10]:


if __name__ == '__main__':
    app.run(port=51393)
    


# In[ ]:




