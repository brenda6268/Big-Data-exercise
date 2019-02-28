#Get RMSE
'''
Now that you know how to build a model and generate predictions, and have an evaluator to tell us how well it predicts ratings, we can calculate the RMSE to see how well an ALS model performed. We'll use the evaluator that we built in the previous exercise to calculate and print the rmse.

Instructions
100 XP
Call the .evaluate() method on our evaluator to calculate our RMSE on the test_predictions dataframe. Call the result RMSE.
Print the RMSE
'''

# Code
# Evaluate the "test_predictions" dataframe
RMSE = evaluator.evaluate(test_predictions)

# Print the RMSE
print (RMSE)

'''result
0.16853197489754093

'''