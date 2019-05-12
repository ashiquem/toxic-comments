from flask import Flask, render_template, request
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import tensorflow as tf
import pickle
import sys
import os


app = Flask(__name__)

MAXLEN = 256
BASE_PATH = os.getcwd() + '/webapp'

model = None
tokenizer = None
graph = None

def load():
    global model
    global tokenizer
    global graph
    
    graph = tf.get_default_graph()
    model = load_model(BASE_PATH+'/model.h5')
    with open(BASE_PATH + '/tokenizer.pickle','rb') as handle:
        tokenizer = pickle.load(handle)
    sys.stdout.write('load complete')
    return

load()

def preprocess(text):
    sequence = pad_sequences(tokenizer.texts_to_sequences([text]),MAXLEN)
    return sequence


def predict(text):
    classes = ['Toxic','Severly Toxic','Obscene','Threat','Insult','Identity Hate']
    outputs = model.predict(preprocess(text))
    result = {}
    for i,score in enumerate(outputs[0]):
        result[classes[i]]= '{:.1f}%'.format(score*100)
    
    return result


@app.route("/")
def index():

    return render_template("master.html")

@app.route("/go")
def go():
    text = request.args.get('query','')
    with graph.as_default():
        result = predict(text)
    
    return render_template("go.html",result=result,comment=text)

if __name__ =='main':
    load()
    app.run()
    