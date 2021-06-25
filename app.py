## import library 

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

## create Flask app 
app = Flask(__name__)


## load Pretrained model 
with open('gbc.pickle', 'rb') as f:
    loaded_model = pickle.load(f)


## return to Home Page 
@app.route('/')
def home_page():
	return render_template('form.html')


## git Data from Post Request 
@app.route('/predict1' ,  methods=['POST' ,'GET'])
def predict():
	op1 =""
	
	data = [

			request.form['Gender'],
			request.form['Age'],
			request.form['Driving_License'],
			request.form['Region_Code'],
			request.form['Previously_Insured'],
			request.form['Vehicle_Age'],
			request.form['Vehicle_Damage'],
			request.form['Annual_Premium'],
			request.form['Policy_Sales_Channel'],
			request.form['Vintage']
		]


	data = np.array([np.asarray((data), dtype=float)])
	predictions = loaded_model.predict(data)
	
	if predictions[0] == 1:
		op1 = 'interested'
	else:
		op1 = 'not interested'
	return render_template('form.html' , pred = op1)
	


## rum Main application 
if __name__ == "__main__":
	app.run(debug = True)

