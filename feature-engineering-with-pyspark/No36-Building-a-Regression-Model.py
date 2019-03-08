#Building a Regression Model
'''
One of the great things about PySpark ML module is that most algorithms can be tried and tested without changing much code. Random Forest Regression is a fairly simple ensemble model, using bagging to fit. Another tree based ensemble model is Gradient Boosted Trees which uses a different approach called boosting to fit. In this exercise let's train a GBTRegressor.

Instructions
70 XP

Import GBTRegressor from pyspark.ml.regression which you will notice is the same module as RandomForestRegressor.
Instantiate GBTRegressor with featuresCol set to the vector column of our features named, features, labelCol set to our dependent variable, SALESCLOSEPRICE and the random seed to 42
Train the model by calling fit() on gbt with the imported training data, train_df.
'''

# Code

from pyspark.ml.regression import GBTRegressor

# Train a Gradient Boosted Trees (GBT) model.
gbt = GBTRegressor(featuresCol="features",
                           labelCol='SALESCLOSEPRICE',
                           predictionCol="Prediction_Price",
                           seed=42
                           )

# Train model.
model = gbt.fit(train_df)


'''
note:as you can see switching from RandomForestRegressor
 to GBTRegressor was very easy to do. In practice you should 
 try multiple algorithms and evaluate which one fits your data best.
 '''