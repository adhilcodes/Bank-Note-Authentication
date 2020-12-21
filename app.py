from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)


pickle_in = open(r"./classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def home():
      return render_template("index.html")

#Get method

@app.route('/predict', methods=['POST'])
def predict():
      

      in_features = [float(x) for x in request.form.values()]
      final_features = [np.array(in_features)]
      prediction = classifier.predict(final_features)
      final_prediction = str(prediction)
      
      return render_template("index.html", prediction_text="Predicted value is {}".format(final_prediction))

if __name__ == "__main__":
      app.run(debug=True)
