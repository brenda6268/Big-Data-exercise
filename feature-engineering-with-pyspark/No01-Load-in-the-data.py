#Load in the data
'''
Reading in data is the first step to using PySpark for data science! Let's leverage the new industry standard of parquet files!

Instructions
100 XP
Use the parquet() file reader to read in 'Real_Estate.parq' as described in the video exercise.
Print out the list of columns with columns.
'''
# Code

# Read the file into a dataframe
df = spark.read.parquet('Real_Estate.parq')
# Print columns in dataframe
print(df.columns)


