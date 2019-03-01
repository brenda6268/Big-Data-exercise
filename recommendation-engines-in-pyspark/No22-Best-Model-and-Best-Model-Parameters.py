#Best Model and Best Model Parameters
'''
Now we have our cross validator ("cv") built out. We can now tell Spark to take our data, fit the ALS algorithm to it, and try the different combinations of hyperparameter values from our param_grid so it can identify what values provide the smallest rmse. Unfortunately, this takes too long to complete here, but for your reference, this is how it is done:

#Fit cross validator to the 'train' dataset
model = cv.fit(train)

#Extract best model from the cv model above
best_model = model.bestModel
This code has been run separately, and the best_model has been identified. Use the commands given to extract the parameters of the model.

Instructions
100 XP

Print type(best_model) to confirm that the model ALS built from our hyperparameter options is indeed completed. A print statement is needed here in order to work with subsequent print statements.
Extract the rank from the best_model by calling the .getRank() method on the best_model.
Extract the maxIter from the best_model by calling the .getMaxIter() method on the best_model.
Extract the regParam from the best_model by calling the .getRegParam() method on the best_model.
'''

# Code

# Print best_model
print(type(best_model))

# Complete the code below to extract the ALS model parameters
print("**Best Model**")

# Print "Rank"
print("  Rank:", best_model.getRank())

# Print "MaxIter"
print("  MaxIter:", best_model.getMaxIter())

# Print "RegParam"
print("  RegParam:", best_model.getRegParam())

'''result
<class 'pyspark.ml.recommendation.ALS'>
**Best Model**
  Rank: 50
  MaxIter: 100
  RegParam: 0.1
'''

'''note
 notice, the best hyperparameter values were all in the middle of the ranges we provided.
  If they were on the low or high end, we would simply adjust our ranges accordingly. 
  Given that they were in the middle, we could tune even further by narrowing our range 
  to get even more precise hyperparameter values.
'''