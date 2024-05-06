# Diabetes_prediction

1.  First we read the dataset
2.  Then analyze tha dataset what columns it contans,is there any null values,what are input features what is output like that
3.  3.Define  the dataset into x attributes(which we take as input) and y attributes which give prediction(generally last column)
4.  Applying standard scaler to x to make all attributes of x within the range of 0 to 1.
5.  Now,split our dataset into train and test data in the ratio of  8 : 2
6.  After that applying the algorithm.In this model we apply SVM algorithm with linear kernel .In svm we have three kernels i.e, linear kernel is used for Binary 
    classification and polynomial,RBF are used for Multiclass classification.
7. Now,its time to find accuracy.In our model the training accuracy is 78 percent and testing accuracy is 77 percent.
8. Now,I need to save the model by using pickle module. 
