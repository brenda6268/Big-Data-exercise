#Interactive Use of PySpark
'''
PySpark shell is an interactive shell for basic testing and debugging but it is quite powerful. The easiest way to demonstrate the power of PySpark’s shell is to start using it. In this example, you'll load a simple list containing numbers ranging from 1 to 100 in the PySpark shell.

The most important thing to understand here is that we are not creating any SparkContext object because PySpark automatically creates the SparkContext object named sc, by default in the PySpark shell.

Instructions

Create a python list named numb containing the numbers 1 to 100.
Load the list into Spark using Spark Context's parallelize method and assign it to a variable spark_data.
'''

#code
# Create a python list of numbers from 1 to 100 
numb = range(1, 100)

# Load the list into PySpark  
spark_data = sc.parallelize(numb)#use parallelize() create a RDD, the elements in the list are partitioned automatically, and sent to different machine.
spark_data



'''result
 PythonRDD[2] at RDD at PythonRDD.scala:49


'''

spark_data.getNumPartitons()#check how many part split
'''result

Out[4]: 4
'''

spark_data.glom().collect()# if a 4-core laptop, will be 4. This is dangerous method for memory. donn't use.
'''result
[[1,
  2,
  3,
  4,
  .
  .
  .
    24],
 [25,
 .
 .
  49],
 [50,
 .
 .
  74],
 [75,
 .
 .
 98,
  99]]

'''
