#Create a base RDD and transform it
'''
The volume of unstructured data (log lines, images, binary files) in existence is growing dramatically, and PySpark is an excellent framework for analyzing this type of data through RDDs. In this 3 part exercise, you will write code that calculates the most common words from Complete Works of William Shakespeare.

Here are the brief steps for writing the word counting program:

Create a base RDD from Complete_Shakespeare.txt file.
Use RDD transformation to create a long list of words from each element of the base RDD.
Remove stop words from your data.
Create pair RDD where each element is a pair tuple of ('w', 1)
Group the elements of the pair RDD by key (word) and add up their values.
Swap the keys (word) and values (counts) so that keys is count and value is the word.
Finally, sort the RDD by descending order and print the 10 most frequent words and their frequencies.
In this first exercise, you'll create a base RDD from Complete_Shakespeare.txt file and transform it to create a long list of words.

Remember, you already have a SparkContext sc already available in your workspace. A file_path variable (which is the path to the Complete_Shakespeare.txt file) is also loaded for you.

Instructions
100 XP
Create an RDD called baseRDD that reads lines from file_path.
Transform the baseRDD into a long list of words and create a new splitRDD.
Count the total words in splitRDD.
'''

# Code
# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split(" "))

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())

'''
Total number of words in splitRDD: 1410671
'''