#Loading data in PySpark shell
'''
In PySpark, we express our computation through operations on distributed collections that are automatically parallelized across the cluster. In the previous exercise, you have seen an example of loading a list as parallelized collections and in this exercise, you'll load the data from a local file in PySpark shell.

Remember you already have a SparkContext sc and file_path variable (which is the path to the README.md file) already available in your workspace.

Instructions
100 XP
Load a local text file README.md in PySpark shell.
'''

#code
# Load a local file into PySpark shell
lines = sc.textFile(file_path)