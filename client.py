#!/usr/bin/env python
# coding: utf-8

# In[4]:


from CyClient import *
import speech_recognition as sr
from CyClient import *
from flask_cors import CORS


revdicto=revdicto_maker()
app = Flask(__name__)
CORS(app)
r = sr.Recognizer()
def main_function(vector,):
    ans=[]
    for m in vector:
        cipher=Pallier_encrpyt(m)
        ans.append(cipher)
    return ans


@app.route('/')
def home():
    return render_template('ROOM.html')


@app.route('/predict',methods=['POST'])
def predict():
    print('audio request received, speech-to-text in progress')
    f = request.files['audio_data']
    f.save('audio.wav')

    sound=sr.AudioFile('audio.wav')
    with sound as source:
        audio = r.record(source)

    text=r.recognize_google(audio, language='en-in')

    print("================================================")
    print('input string: ',text)
    print("================================================")

    input_vector=aggressive_fermenter(text)

    print("================================================")
    print('\ninput_vector: ', input_vector)
    print("================================================")

    output_ans=main_function(input_vector)
    # keys=print_keys()
    print("\nencrypted vector ",output_ans)
        
    

    res = requests.post('http://127.0.0.1:51393/ml_encrypted', json={'array':output_ans}).json()
    print('\nrecieved ML output: ',res['res'])
    decrypt_ans=[]
    decrypt_vector=res['res']
    for i in decrypt_vector:
        decrypt_ans.append(Pallier_decrpyt(int(i)))
    print('\ndecrypted score output: ',decrypt_ans)
    restask=decrypt_ans.index(max(decrypt_ans))
    restext=revdicto[restask]
    print('\nresult sent: ',restext)
    print(restask)
    return str(restask)

#for handliing request of unencrypted data
@app.route('/unencrypted',methods=['POST'])
def unencrypted():
    print('audio request received, speech-to-text in progress')
    f = request.files['audio_data']
    f.save('audio.wav')

    sound=sr.AudioFile('audio.wav')
    with sound as source:
        audio = r.record(source)

    text=r.recognize_google(audio, language='en-in')

    print("================================================")
    print('input string: ',text)
    print("================================================")

    input_vector=aggressive_fermenter(text)

    print("================================================")
    print('\ninput_vector: ', input_vector)
    print("================================================") 

    res = requests.post('http://127.0.0.1:51393/ml_fraud', json={'array':input_vector}).json()
    print('\nrecieved ML output: ',res['res'])
    decrypt_ans=[]
    decrypt_vector=res['res']
    restask=decrypt_ans.index(max(decrypt_ans))
    restext=revdicto[restask]
    print('\nresult sent: ',restext)
    print(restask)
    return str(restask)


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/', new=2)
    app.run()


# In[ ]:


# In[ ]:




