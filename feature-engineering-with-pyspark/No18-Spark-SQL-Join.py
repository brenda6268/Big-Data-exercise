#Spark SQL Join
'''
Sometimes it is much easier to write complex joins in SQL. In this exercise, we will start with the join keys already in the same format and precision but will use SparkSQL to do the joining.

Instructions
100 XP
Register the Dataframes as SparkSQL tables with createOrReplaceTempView, name them the df and walk_df respectively.
In the join_sql string, set the left table to df and the right table to walk_df
Call spark.sql() on the join_sql string to perform the join.
'''

# Code
# Register dataframes as tables
df.createOrReplaceTempView('df')
walk_df.createOrReplaceTempView('walk_df')

# SQL to join dataframes
join_sql = 	"""
			SELECT 
				*
			FROM df
			LEFT JOIN walk_df
			ON df.longitude = walk_df.longitude
			AND df.latitude = walk_df.latitude
			"""
# Perform sql join
joined_df = spark.sql(join_sql)
