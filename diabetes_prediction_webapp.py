import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model=pickle.load(open('new_trained_model.sav','rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1) # here we are reshaping the data to one row because if we dont reshape thn the system will wait for the total data to accept.

    # standardizing the sample
    #std_data=scaler.transform(input_data_reshaped)

    prediction=loaded_model.predict(input_data_reshaped)

    print(prediction)

    if prediction==0:
      return 'the person is not diabetic'
    else:
      return 'the person is diabetic'



def main():
    # giving a title
    st.title('diabetes web app')
    
    # getting  the input from the user
    #Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
    
    Pregnancies=st.text_input('number of pregnencies')
    Glucose=st.text_input('glucose level')
    BloodPressure=st.text_input('blood presure value')
    SkinThickness=st.text_input('skin thickness value')
    Insulin=st.text_input('insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age=st.text_input('age of the person')
    
    # code for prediction
    diagonosis=''
    
    # creating a button for prediction
    if st.button('Diabetes test result'):
        diagonosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    

    st.success(diagonosis)



if __name__=='__main__':
    main()


