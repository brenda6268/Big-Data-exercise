#Build RMSE Evaluator
'''
Now that you know how to fit a model to training data and generate test predicitons, you need a way to evaluate how well your model performs. For this we'll build an evaluator. Evaluators in Spark can be built out in various ways. For our purposes here, we want a regressionEvaluator that caclucates the RMSE. After we build our our regressionEvaluator, we can fit the model to our data and generate predictions.

Instructions
100 XP

Import the required RegressionEvaluator package from the pyspark.ml.evaluation class
Complete the evaluator code build out specifying the metric name to be "rmse", set the labelCol to the name of the column in our ratings data that contains our ratings (use the ratings.columns method in case you forgot from the previous exercise) and set the prediction column name to "prediction".
Confirm that the evaluator was properly created by extracting each of the three parameters from it. Do this by running the following 3 lines of code each within a print statement:
evaluator.getMetricName()
evaluator.getLabelCol()
evaluator.getPredictionCol()
'''

#code
# Import RegressionEvaluator
from pyspark.ml.evaluation import RegressionEvaluator

# Complete the evaluator code
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")

# Extract the 3 parameters
print (evaluator.getMetricName())
print (evaluator.getLabelCol())
print (evaluator.getPredictionCol())

'''
rmse
rating
prediction

'''