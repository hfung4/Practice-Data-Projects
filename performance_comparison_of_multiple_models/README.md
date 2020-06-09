**The purpose of this notebook is to present ways in which we can compare multiple statistical learning approaches for a dataset**
- For simplicity, I will use a toy dataset (breast cancer classification problem) from sklearn.
- I will write a function that outputs a DataFrame that contains k estimated test error/accuracy (from CV) for each of the 6 models.
- Next I will bootstrap 30 samples of the CV performance measures (time and fit) for each of the 6 models.
- I will use data visualization to compare the average performance measures (time and fit) across the models.


**I also wrote another function that (in a compact way) perform GridSearch on multiple models**
- Create a pipeline that standardize the train data, then optimize and fit the model with GridSearchCV
- Get a list of "optimized" models 
- Compare the optimized models and choose the "best" statistical learning approach based on highest AUC score (on the test dataset)
