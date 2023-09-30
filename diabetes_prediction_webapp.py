
import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load((open("C:/Users/WIN10/Desktop/ML DATASETS/trained_model (1).sav",'rb')))

#creating a function
def diabetis_prediction(input_data):
  print(input_data)
  #input_data=(5,166,72,19,175,25.8,0.587,51)
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=loaded_model.predict( input_data_reshaped)
  print(prediction)
  if (prediction==0):
    return "The Person is not Diabetic"
  else:
    return "The Person is Diabetic" 
   
    
   
def main():
     #giving a title
     st.title('Diabetis preddiction Web App')
        
     #getting the input data from the user
       
        
     Pregnancies = st.text_input('Number of Pregnancies')
     Glucose = st.text_input('Glucose Level')
     BloodPressure = st.text_input('Blood Pressure value')
     SkinThickness = st.text_input('Skin Thickness Value')
     Insulin = st.text_input('Insulin Level')
     BMI = st.text_input('BMI value')
     DiabetesPedigreeFunction = st.text_input('Diabetis Pedigree Function Value')
     Age = st.text_input('Age of the Person')
        
        
     #code for prediction
     diagnosis = " "
        
     #creating a button for prediction
     if  st.button("Diabetis Test Result"):
         diagnosis=diabetis_prediction([ Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
            
     st.success(diagnosis)    
        
        
        
if __name__ == '__main__':
    main()       
            
        
        
