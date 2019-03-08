#One Hot Encoding
'''
In the United States where you live determines which schools your kids can attend. Therefore it's understandable that many people care deeply about which school districts their future home will be in. While the school districts are numbered in SCHOOLDISTRICTNUMBER they are really categorical. Meaning that summing or averaging these values has no apparent meaning. Therefore in this example we will convert SCHOOLDISTRICTNUMBER from a categorial variable into a numeric vector to use in our machine learning model later.

Instructions
100 XP

Instantiate a StringIndexer transformer called string_indexer with SCHOOLDISTRICTNUMBER as the input and School_Index as the output.
Apply the transformer string_indexer to df with fit() and transform(). Store the transformed dataframe in indexed_df.
Create a OneHotEncoder transformer called encoder using School_Index as the input and School_Vec as the output.
Apply the transformation to indexed_df using transform(). Inspect the iterative steps of the transformation with the supplied code.
'''

# Code
from pyspark.ml.feature import OneHotEncoder, StringIndexer

# Map strings to numbers with string indexer
string_indexer = StringIndexer(inputCol='SCHOOLDISTRICTNUMBER', outputCol='School_Index')
indexed_df = string_indexer.fit(df).transform(df)

# Onehot encode indexed values
encoder = OneHotEncoder(inputCol='School_Index', outputCol='School_Vec')
encoded_df = encoder.transform(indexed_df)

# Inspect the transformation steps
encoded_df[['SCHOOLDISTRICTNUMBER', 'School_Index', 'School_Vec']].show(truncate=100)

'''result
<script.py> output:
    +-----------------------------+------------+-------------+
    |         SCHOOLDISTRICTNUMBER|School_Index|   School_Vec|
    +-----------------------------+------------+-------------+
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |622 - North St Paul-Maplewood|         1.0|(7,[1],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |622 - North St Paul-Maplewood|         1.0|(7,[1],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    |             834 - Stillwater|         3.0|(7,[3],[1.0])|
    +-----------------------------+------------+-------------+
    only showing top 20 rows


note: One Hot Encoding is a great way to handle categorial variables.
 You may have noticed that the implementation in PySpark is different 
 than Pandas get_dummies() as it puts everything into a single column
  of type vector rather than a new column for each value. It's also 
  different from sklearn's OneHotEncoder in that the last categorical
   value is captured by a vector of all zeros.
'''