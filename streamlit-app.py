## import library 

import streamlit as st
import pickle
import numpy as np
import pandas as pd


## glopal variable 
op1 = " "
gender = 0

## function to predict output 
def predict_output(data):
	with open('gbc.pickle', 'rb') as f:
		loaded_model = pickle.load(f)
	
	predictions = loaded_model.predict(data)
	
	return predictions[0]


## main application 
def main():

	## set background image 
	st.markdown("<h1 style='text-align: center; color: black;'> Up-size Existing Customer Utilization</h1>", unsafe_allow_html=True)
	st.markdown(
		  """
		  <style>
		  .reportview-container {
		    background: url("https://th.bing.com/th/id/R3c363a11aecebd7e76f18f23f81e5c2e?rik=xBXL%2bdFNrjtLSA&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fCy7YPNg.jpg&ehk=QtoG1zotzCDq%2beIQ7SHA6xKvIQZaZGm13fK7HoOLxXA%3d&risl=&pid=ImgRaw")
		  }

		  </style>
		  """,
		  unsafe_allow_html=True
  				)


	## input columns 

	##  row 1	
	col1, col2 = st.beta_columns(2)
	with col1:
		Gender = st.text_input("Gender" , key ='Gender')

	with col2:	
		Age = st.text_input("Age" , key = 'Age')

	## row 2

	col1, col2 = st.beta_columns(2)
	with col1:
		Driving_License = st.text_input("Driving License" , key ='Driving_License')

	with col2:	
		Region_Code = st.text_input("Region Code" , key = 'Region_Code')

	## row 3
	col1, col2 = st.beta_columns(2)
	with col1:
		Previously_Insured = st.text_input("Previously Insured" , key ='Previously_Insured')

	with col2:	
		Vehicle_Age = st.text_input("Vehicle Age" , key = 'Vehicle_Age')

	## row 4
	col1, col2 = st.beta_columns(2)
	with col1:
		Vehicle_Damage = st.text_input("Vehicle Damage" , key ='Vehicle_Damage')

	with col2:	
		Annual_Premium = st.text_input("Annual Premium" , key = 'Annual Premium')

	## row 5	
	col1, col2 = st.beta_columns(2)
	with col1:
		Policy_Sales_Channel = st.text_input("Policy Sales Channel" , key ='Policy_Sales_Channel')

	with col2:	
		Vintage = st.text_input("Vintage" , key = 'Vintage')


	## PREDICT OUTPUT 

	## output 
	cols = st.beta_columns(5)

	center_button = st.button('Predict Output')
	if center_button == 1:
		if Gender == 'male':
			gender = 1
		else:
			gender = 0

		data = [gender,Age,Driving_License,Region_Code,Previously_Insured,
		   Vehicle_Age,Vehicle_Damage,Annual_Premium,
		   Policy_Sales_Channel,Vintage]
	
		data = np.array([np.asarray((data), dtype=float)])
		
		op1 = predict_output(data)
		if op1 == 1:
			#op1 = 'interested'
			st.markdown("<h1 style='text-align: center; color: black;'> This Person Is Interested </h1>", unsafe_allow_html=True)

		else:
			op1 = 'not interested'
			st.markdown("<h1 style='text-align: center; color: black;'> This Person Not Interested </h1>", unsafe_allow_html=True)




	


if __name__ == '__main__':
	main()
	