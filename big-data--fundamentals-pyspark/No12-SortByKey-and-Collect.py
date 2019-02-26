#SortByKey and Collect
'''
Many times it is useful to sort the pair RDD based on the key (for example word count which you'll see later in the chapter). In this exercise, you'll sort the pair RDD Rdd_Reduced that you created in the previous exercise into descending order and print the final output.

Remember, you already have a SparkContext sc and Rdd_Reduced available in your workspace.

Instructions
100 XP
Sort the Rdd_Reduced RDD using the key in descending order.
Collect the contents and iterate to print the output.
'''

# Code
# Sort the reduced RDD with the key by descending order
Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)

# Iterate over the result and print the output
for num in Rdd_Reduced_Sort.collect():
  print("Key {} has {} Counts".format(num[0], num[1]))

  '''
Key 4 has 5 Counts
Key 3 has 10 Counts
Key 1 has 2 Counts
  '''