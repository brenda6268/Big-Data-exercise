#Create test/train splits and build your ALS model
'''
You already know how to build an ALS model having done it in the previous chapter. We will do that again here, but we'll take some additional steps to fully build out a cross-validated model. First let's import the requisite packages and create our train and test data sets in preparation for the cross validation step.

Instructions
100 XP

Import the RegressionEvaluator from the ml.evaluation class, the ALS algorithm from the ml.recommendation class, and the ParamGridBuilder and the CrossValidator from the ml.tuning class.
Create an .80/.20 train/test split on the ratings data using the randomSplit method. Name the datasets train and test, and set the random seed to 1234.
Build out the ALS model telling Spark the names of the columns in the ratings dataframe that correspond to the userCol, itemCol and ratingCol. Set the nonnegative argument to True, the coldStartStrategy to "drop" and let Spark know that these are not implicitPrefs by setting the implicitPrefs argument to False. Call this model "als".
Verify that the model was created by simply calling the type() function on the als model. The output should indicate what type of model it is.
'''

# Code
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Create test and train set
(train, test) = ratings.randomSplit([0.8, 0.2], seed = 1234)

# Create ALS model
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", nonnegative = True, coldStartStrategy="drop",implicitPrefs = False)

# Confirm that a model called "als" was created
type(als)


'''result
pyspark.ml.recommendation.ALS
'''