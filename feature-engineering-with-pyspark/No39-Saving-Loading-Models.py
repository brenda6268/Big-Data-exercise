#Saving & Loading Models
'''
Often times you may find yourself going back to a previous model to see what assumptions or settings were used when diagnosing where your prediction errors were coming from. Perhaps there was something wrong with the data? Maybe you need to incorporate a new feature to capture an unusual event that occurred?

In this example, you will practice saving and loading a model.

Instructions
100 XP

Import RandomForestRegressionModel from pyspark.ml.regression.
Using the model in memory called model call the save() method on it and name the model rfr_no_listprice.
Reload the saved model file rfr_no_listprice by calling load() on RandomForestRegressionModel and storing it into loaded_model.
'''

# Code
from pyspark.ml.regression import RandomForestRegressionModel

# Save model
model.save('rfr_no_listprice')

# Load model
loaded_model = RandomForestRegressionModel.load('rfr_no_listprice')