#PySpark MLlib algorithms
'''
Before using any Machine learning algorithms in PySpark shell, you'll have to import the submodules of pyspark.mllib library and then choose the appropriate class that is needed for a specific machine learning task.

In this simple exercise, you'll learn how to import the different submodules of pyspark.mllib along with the classes that are needed for performing Collaborative filtering, Classification and Clustering algorithms.

Instructions
100 XP

Import pyspark.mllib recommendation submodule and Alternating Least Squares class.
Import pyspark.mllib classification submodule and Logistic Regression with LBFGS class.
Import pyspark.mllib clustering submodule and kmeans class.
'''

# Code

# Import the library for ALS
from pyspark.mllib.recommendation import ALS

# Import the library for Logistic Regression
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

# Import the library for Kmeans
from pyspark.mllib.clustering import KMeans