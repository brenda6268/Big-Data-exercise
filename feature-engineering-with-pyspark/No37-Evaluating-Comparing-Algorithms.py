#Evaluating & Comparing Algorithms
'''
Now that we've created a new model with GBTRegressor its time to compare it against our baseline of RandomForestRegressor. To do this we will compare the predictions of both models to the actual data and calculate RMSE and R^2.

Instructions
100 XP

Import RegressionEvaluator from pyspark.ml.evaluation so it is available for use later.
Initialize RegressionEvaluator by setting labelCol to our actual data, SALESCLOSEPRICE and predictionCol to our predicted data, Prediction_Price
To calculate our metrics, call evaluate on evaluator with the prediction values preds and create a dictionary with key evaluator.metricName and value of rmse, do the same for the r2 metric.
'''

# Code
from pyspark.ml.evaluation import RegressionEvaluator

# Select columns to compute test error
evaluator = RegressionEvaluator(labelCol='SALESCLOSEPRICE', 
                                predictionCol='Prediction_Price')
# Dictionary of model predictions to loop over
models = {'Gradient Boosted Trees': gbt_predictions, 'Random Forest Regression': rfr_predictions}
for key, preds in models.items():
  # Create evaluation metrics
  rmse = evaluator.evaluate(preds, {evaluator.metricName: "rmse"})
  r2 = evaluator.evaluate(preds, {evaluator.metricName: "r2"})
  
  # Print Model Metrics
  print(key + ' RMSE: ' + str(rmse))
  print(key + ' R^2: ' + str(r2))

  '''result
<script.py> output:
    Random Forest Regression RMSE: 22898.84041072095
    Random Forest Regression R^2: 0.9666594402208077
    Gradient Boosted Trees RMSE: 74380.63652512032
    Gradient Boosted Trees R^2: 0.6482244200795505
  '''