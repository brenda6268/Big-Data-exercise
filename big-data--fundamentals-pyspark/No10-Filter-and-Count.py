#Filter and Count
'''
The RDD transformation filter() returns a new RDD containing only the elements that satisfy a particular function. It is useful for filtering large datasets based on a keyword. For this exercise, you'll filter out lines containing keyword Spark from fileRDD RDD which consists of lines of text from the README.md file. Next, you'll count the total number of lines containing the keyword Spark and finally print the first 4 lines of the filtered RDD.

Remember, you already have a SparkContext sc, file_path and fileRDD available in your workspace.

Instructions
100 XP
Create filter() transformation to select the lines containing the keyword Spark.
How many lines in fileRDD_filter contains the keyword Spark?
Print the first four lines of the resulting RDD.
'''

# Code
# Filter the fileRDD to select lines with Spark keyword
fileRDD_filter = fileRDD.filter(lambda line: 'Spark' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is", fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4):    # fileRDD_filter.take(4) is a list. and can be print out by print()
  print(line)

  '''

The total number of lines with the keyword Spark is 7
Examples for Learning Spark
Examples for the Learning Spark book. These examples require a number of libraries and as such have long build files. We have also added a stand alone example with minimal dependencies and a small build file
These examples have been updated to run against Spark 1.3 so they may
be slightly different than the versions in your copy of "Learning Spark".

  '''

  In [3]: print(fileRDD_filter.take(4))
  '''
['Examples for Learning Spark', 'Examples for the Learning Spark book. These examples require a number of libraries and as such have long build files. We have also added a stand alone example with minimal dependencies and a small build file', 'These examples have been updated to run against Spark 1.3 so they may', 'be slightly different than the versions in your copy of "Learning Spark".']