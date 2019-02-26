#Remove stop words and reduce the dataset
'''
After splitting the lines in the file into a long list of words using flatMap() transformation, in the next step, you'll remove stop words from your data. Stop words are common words that are often uninteresting. For example "I", "the", "a" etc., are stop words. You can remove many obvious stop words with a list of your own. But for this exercise, you will just remove the stop words from a curated list stop_words provided to you in your environment.

After removing stop words, you'll next create a pair RDD where each element is a pair tuple (k, v) where k is the key and v is the value. In this example, pair RDD is composed of (w, 1) where w is for each word in the RDD and 1 is a number. Finally, you'll combine the values with the same key from the pair RDD.

Remember you already have a SparkContext sc and splitRDD available in your workspace.

Instructions
100 XP

Convert the words in splitRDD in lower case and then remove stop words from stop_words.
Create a pair RDD tuple containing the word and the number 1 from each word element in splitRDD.
Get the count of the number of occurrences of each word (word frequency).
'''

# Code
# Convert the words in lower case and remove stop words from stop_words
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1 
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)
