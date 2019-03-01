#Tell Spark how to tune your ALS model
'''
Now we'll need to create a ParamGrid to tell Spark what hyperparameters we want it to tune, how to tune them, and then build out an evaluator so Spark can know how to measure the algorithm's performance.

Instructions
100 XP

Import the RegressionEvaluator from the pyspark.ml.evaluation class and the ParamGridBuilder and CrossValidator from the pyspark.ml.tuning class.

Build a ParamGrid called param_grid using the ParamGridBuilder provided. Call the .addGrid method on each hyperparameter by providing the name of the model and the name of each hyperparameter (ex: .addGrid(als.rank, []). Do this for the rank, maxIter and regParam hyperparameters. Also provide the respective lists of hyperparameter values that Spark should try, as provided here:

rank: [10, 50, 100, 150]
maxIter: [5, 50, 100, 200]
regParam: [.01, .05, .1, .15]

Create a RegressionEvaluator called "evaluator". Set the metricName to "rmse", set the labelCol to "rating", and tell Spark that when it generates predictions to call the predictionCol "prediction".

Run len(param_grid) to confirm that the param_grid was created and to confirm that the right number of hyperparameter combinations will be tested. It should be equal to the number of rank values * the number of maxIter values * the number of regParam values in the ParamGridBuilder.
'''

# Code
# Import the requisite items
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Add hyperparameters and their respective values to param_grid
param_grid = ParamGridBuilder() \
            .addGrid(als.rank, [10, 50, 100, 150]) \
            .addGrid(als.maxIter, [5, 50, 100, 200]) \
            .addGrid(als.regParam, [.01, .05, .1, .15]) \
            .build()
           
# Define evaluator as RMSE and print length of evaluator
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction") 
print ("Num models to be tested: ", len(param_grid))

'''result
Num models to be tested:  64
'''