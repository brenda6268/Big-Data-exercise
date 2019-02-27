#Model training and predictions
'''
After splitting the data into training and test data, in the second part of the exercise, you'll train the ALS algorithm using the training data. PySpark MLlib's ALS algorithm has the following mandatory parameters - rank (the number of latent factors in the model) and iterations (number of iterations to run). After training the ALS model, you can use the model to predict the ratings from the test data. For this, you will provide the user and item columns from the test dataset and finally print the first 2 rows of predictAll() output.

Remember, you have SparkContext sc, trainingdata and testdata are already available in your workspace.

Instructions
100 XP

Train ALS algorithm with training data and configured parameters (rank = 10 and iterations = 10).
Drop the rating column in the test data.
Test the model by predicting the rating from the test data.
Print the first two rows of the predicted ratings.
'''

# Code
# Create the ALS model on the training data
model = ALS.train(training_data, rank=10, iterations=10)

# Drop the ratings column 
testdata_no_rating = test_data.map(lambda p: (p[0], p[1]))

# Predict the model  
predictions = model.predictAll(testdata_no_rating)

# Print the first rows of the RDD
predictions.take(2)

'''
[Rating(user=548, product=1084, rating=3.6608543764664554),
 Rating(user=96, product=1084, rating=3.5842742021340053)]
'''