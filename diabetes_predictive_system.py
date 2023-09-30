# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle


loaded_model=pickle.load(open('D:/mine_/code files @@/python/python_ml_webapp/diabetes_webapp/new_trained_model.sav','rb'))


input_data=(5,166,72,19,175,25.8,0.587,51)
input_data_as_numpy_array=np.asarray(input_data)
print(type(input_data_as_numpy_array))
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1) # here we are reshaping the data to one row because if we dont reshape thn the system will wait for the total data to accept.

# standardizing the sample
#std_data=scaler.transform(input_data_reshaped)

prediction=loaded_model.predict(input_data_reshaped)

print(prediction)

if prediction==0:
  print('the person is non diabetic')
else:
  print('the person is diabetic')