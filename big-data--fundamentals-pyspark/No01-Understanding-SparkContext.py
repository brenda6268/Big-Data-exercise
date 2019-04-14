#Understanding SparkContext
'''
A SparkContext represents the entry point to Spark functionality. It's like a key to your car. PySpark automatically creates a SparkContext for you in the PySpark shell (so you don't have to create it by yourself) and is exposed via a variable sc.

In this simple exercise, you'll find out the attributes of the SparkContext in your PySpark shell which you'll be using for the rest of the course.

Instructions
100 XP
Print the version of SparkContext in the PySpark shell.
Print the Python version of SparkContext in the PySpark shell.
What is the master of SparkContext in the PySpark shell?
'''

#Code
# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)



'''result:
The version of Spark Context in the PySpark shell is 2.3.1
The Python version of Spark Context in the PySpark shell is 3.5
The master of Spark Context in the PySpark shell is local[*]
'''
'''
Hadoop/MapReduce: Scalable and fault tolerant framework written in Java
Open source
Batch processing
Apache Spark: General purpose and lightning fast cluster computing system
Open source
Both batch and real-time data processing

PySpark APIs are similar to Pandas and Scikit-learn
PySpark has a default SparkContext called  sc

Master: URL of the cluster or “local” string to run in local mode of SparkContext
'''