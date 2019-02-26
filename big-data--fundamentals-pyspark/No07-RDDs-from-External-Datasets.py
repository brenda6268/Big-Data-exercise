#RDDs from External Datasets
'''
PySpark can easily create RDDs from files that are stored in external storage devices such as HDFS (Hadoop Distributed File System), Amazon S3 buckets, etc. However, the most common method of creating RDD's is from files stored in your local file system. This method takes a file path and reads it as a collection of lines. In this exercise, you'll create an RDD from the file path (file_path) with the file name README.md which is already available in your workspace.

Remember you already have a SparkContext sc available in your workspace.

Instructions
100 XP
Print the file_path in the PySpark shell.
Create an RDD named fileRDD from a file_path with the file name README.md.
Print the type of the fileRDD created.
'''

# Code
# Print the file_path
print("The file_path is", file_path)

# Create a fileRDD from file_path
fileRDD = sc.textFile(file_path)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))

'''
The file_path is /usr/local/share/datasets/README.md
The file type of fileRDD is <class 'pyspark.rdd.RDD'>
'''