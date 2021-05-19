from flask import Flask, url_for, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import io
import base64

load_model = pickle.load(open('model/rf_model.pkl','rb'))
app = Flask(__name__)

def diabetesPredict(test_set) :
    global load_model
    predict = load_model.predict([test_set])[0]
    return predict

@app.route('/')
def index() :
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict() :
    if request.method == 'POST':
        pregnancy = int(request.form.get('pregnancy'))
        glucose = float(request.form.get('glucose'))
        bp = float(request.form.get('bp'))
        st = int(request.form.get('st'))
        insulin = float(request.form.get('insulin'))
        bmi = float(request.form.get('bmi'))
        dpf = float(request.form.get('dpf'))
        age = int(request.form.get('age'))
        test_set = [pregnancy , glucose , bp , st, insulin , bmi , dpf , age]
        print(test_set)
        predict = diabetesPredict(test_set)
        if predict == 0 :
            result = "Negative"
        else :
            result = "Positive"
        return render_template('result.html' , result = result)
    else :
        return render_template('predict.html')

@app.route('/analysis')
def analysis() :
    return render_template('analysis.html')

@app.route('/gallery')
def gallery() :
    return render_template('gallery.html')

@app.route('/about')
def about() :
    return render_template('about.html')

if __name__ == '__main__' :
    app.run(debug=True,port=5001)