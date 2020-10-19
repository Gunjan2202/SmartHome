#!/usr/bin/env python
# coding: utf-8

# In[4]:


from CyClient import *
revdicto=revdicto_maker()
app = Flask(__name__)
def main_function(vector,):
    ans=[]
    for m in vector:
        cipher=Pallier_encrpyt(m)
        ans.append(cipher)
    return ans


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features=request.form.get('experience')
    print('input string: ',int_features)
    input_vector=aggressive_fermenter(int_features)
    print('\ninput_vector: ', input_vector)
    output_ans=main_function(input_vector)
    print("\nencrypted vector ",output_ans)
        
    
    res = requests.post('http://127.0.0.1:51393/ml_encrypted', json={'array':output_ans}).json()
    print('\nrecieved ML output: ',res['res'])
    decrypt_ans=[]
    decrypt_vector=res['res']
    for i in decrypt_vector:
        decrypt_ans.append(Pallier_decrpyt(int(i)))
    print('\ndecrypted score output: ',decrypt_ans)
    restext=revdicto[decrypt_ans.index(max(decrypt_ans))]
    print('\nresult sent: ',restext)
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    # str1=''.join(str(e) for e in decrypt_ans)
    restext=int_features+' : '+restext
    return render_template('index.html', prediction_text=restext)



if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/', new=2)
    app.run()


# In[ ]:


# In[ ]:




