#Loading spam and non-spam data
'''
Logistic Regression is a popular method to predict a categorical response. Probably one of the most common applications of the logistic regression is the message or email spam classification. In this 3-part exercise, you'll create an email spam classifier with logistic regression using Spark MLlib. Here are the brief steps for creating a spam classifier.

Create an RDD of strings representing email.
Run MLlib’s feature extraction algorithms to convert text into an RDD of vectors.
Call a classification algorithm on the RDD of vectors to return a model object to classify new points.
Evaluate the model on a test dataset using one of MLlib’s evaluation functions.
In the first part of the exercise, you'll load the 'spam' and 'ham' (non-spam) files into RDDs, split the emails into individual words and look at the first element in each of the RDD.

Remember, you have a SparkContext sc available in your workspace. Also file_path_spam variable (which is the path to the 'spam' file) and file_path_ham (which is the path to the 'non-spam' file) is already available in your workspace.

Instructions
100 XP

Create two RDDS, one for 'spam' and one for 'non-spam (ham)'.
Split each email in 'spam' and 'non-spam' RDDs into words.
Print the first element in the split RDD of both 'spam' and 'non-spam'.
'''
# code
# Load the datasets into RDDs
spam_rdd = sc.textFile(file_path_spam)
non_spam_rdd = sc.textFile(file_path_non_spam)

# Split the email messages into words
spam_words = spam_rdd.map(lambda email: email.split(' '))
non_spam_words = non_spam_rdd.map(lambda email: email.split(' '))

# Print the first element in the split RDD
print("The first element in spam_words is", spam_words.first())
print("The first element in non_spam_words is", non_spam_words.first())

'''
<script.py> output:
    The first element in spam_words is ['You', 'have', '1', 'new', 'message.', 'Please', 'call', '08712400200.']
    The first element in non_spam_words is ['Rofl.', 'Its', 'true', 'to', 'its', 'name']
'''