#Build Out An ALS Model
'''
Let's specify your first ALS model. Complete the code below to build your first ALS model.


Instructions
100 XP
Use the .columns() method on the ratings data frame to see what the names of the columns are that contain user, movie and ratings data. Print the result. Spark needs to know the names of these columns in order to perform ALS correctly.
Before building our ALS model, we need to split the data into training data and test data. Use the randomSplit() method to split the ratings dataframe into training_data and test_data using an 0.8/0.2 split respectively and a seed for the random number generator of 1234.
Tell Spark which columns contain the userCol, itemCol and ratingCol. Use the .columns method if needed. Complete the hyperparameters. Set the rank to 10, the maxIter to 15, the regParam or lambda to .1, the coldStartStrategy to "drop", the nonnegative argument should be set to True, and since our data contains explicit ratings, set the implicitPrefs argument to False.
Now fit the als model to the training_data portion of the ratings data by calling the als.fit() method on the training_data provided. Call the fitted model model.
Generate predictions on the test_data portion of the ratings data by calling the model.transform() method on the test_data provided. Call the predictions test_predictions. Feel free to view the predictions by calling the .show() method on the test_predictions
'''

# Code

# Split the ratings dataframe into training and test data
(training_data, test_data) = ratings.randomSplit([0.8, 0.2], seed=1234)

# Set the ALS hyperparameters
from pyspark.ml.recommendation import ALS
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", rank =10, maxIter =15, regParam =.1,
          coldStartStrategy="drop", nonnegative =True, implicitPrefs = False)

# Fit the mdoel to the training_data
model = als.fit(training_data)

# Generate predictions on the test_data
test_predictions = model.transform(test_data)
test_predictions.show()

'''result
<script.py> output:
    +------+-------+------+----------+
    |userId|movieId|rating|prediction|
    +------+-------+------+----------+
    +------+-------+------+----------+

'''