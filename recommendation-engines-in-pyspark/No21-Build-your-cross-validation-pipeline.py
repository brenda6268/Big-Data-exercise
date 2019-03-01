#Build your cross validation pipeline
'''
Now that we have our data, our train/test splits, our model and our hyperparameter values, let's tell Spark how to cross validate our model so it can find the best combination of hyperparameters and return it to us.

Instructions
100 XP
Create a CrossValidator called cv with our als model as the estimator, setting estimatorParamMaps to the param_grid you just built. Tell spark that the evaluator to be used is the "evaluator" we built previously. Set the numFolds to 5.
Confirm that our cv was built by simply printing cv.
'''


# Code
# Build cross validator
cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=5)

# Confirm cv was built
print (cv)


'''result
CrossValidator_42b9a9d47dd12f9233dc

'''