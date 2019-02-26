#ReduceBykey and Collect
'''
One of the most popular pair RDD transformations is reduceByKey() which operates on key, value (k,v) pairs and merges the values for each key. In this exercise, you'll first create a pair RDD from a list of tuples, then combine the values with the same key and finally print out the result.

Remember, you already have a SparkContext sc available in your workspace.

Instructions
100 XP

Create a pair RDD named Rdd with tuples (1,2),(3,4),(3,6),(4,5).
Transform the Rdd with reduceByKey() into a pair RDD Rdd_Reduced by adding the values with the same key.
Collect the contents of pair RDD Rdd_Reduced and iterate to print the output.
'''

# Code
# Create PairRDD Rdd with key value pairs
Rdd = sc.parallelize([(1,2),(3,4),(3,6),(4,5)])

# Apply reduceByKey() operation on Rdd
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x+y)

# Iterate over the result and print the output
for num in Rdd_Reduced.collect(): 
  print("Key {} has {} Counts".format(num[0], num[1]))

  '''
Key 4 has 5 Counts
Key 1 has 2 Counts
Key 3 has 10 Counts
  '''