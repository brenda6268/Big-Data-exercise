#Partitions in your data
'''
SparkContext's textFile() method takes an optional second argument called minPartitions for specifying the minimum number of partitions. In this exercise, you'll create an RDD named fileRDD_part with 5 partitions and then compare that with fileRDD that you created in the previous exercise. Refer to the "Understanding Partition" slide in video 2.1 to know the methods for creating and getting the number of partitions in an RDD.

Remember, you already have a SparkContext sc, file_path and fileRDD available in your workspace.

Instructions
100 XP
Instructions
100 XP
Find the number of partitions that support fileRDD RDD.
Create an RDD named fileRDD_part from the file path but create 5 partitions.
Confirm the number of partitions in the new fileRDD_part RDD.
'''

# Code

# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions = 5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())

'''
Number of partitions in fileRDD is 2
Number of partitions in fileRDD_part is 5
'''