#RDDs from Parallelized collections
'''
Resilient Distributed Dataset (RDD) is the basic abstraction in Spark. It is an immutable distributed collection of objects. Since RDD is a fundamental and backbone data type in Spark, it is important that you understand how to create it. In this exercise, you'll create your first RDD in PySpark from a collection of words.

Remember you already have a SparkContext sc available in your workspace.

Instructions
100 XP
Create an RDD named RDD from a list of words.
Confirm the object created is RDD.
'''

#Code
# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))

'''
The type of RDD is <class 'pyspark.rdd.RDD'>

'''