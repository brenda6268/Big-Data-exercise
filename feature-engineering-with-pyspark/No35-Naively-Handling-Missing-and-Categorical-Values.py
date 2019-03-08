#Naively Handling Missing and Categorical Values
'''
Random Forest Regression is robust enough to allow us to ignore many of the more time consuming and tedious data preparation steps. While some implementations of Random Forest handle missing and categorical values automatically, PySpark's does not. The math remains the same however so we can get away with some naive value replacements.

For missing values since our data is strictly positive, we will assign -1. The random forest will split on this value and handle it differently than the rest of the values in the same feature.

For categorical values, we can just map the text values to numbers and again the random forest will appropriately handle them by splitting on them. In this example, we will dust off pipelines from Introduction to PySpark to write our code more concisely. Please note that the exercise will start by displaying the dtypes of the columns in the dataframe, compare them to the results at the end of this exercise.

NOTE: Pipeline and StringIndexer are already imported for you. The list categorical_cols is also available.

Instructions
100 XP

Replace the values in WALKSCORE and BIKESCORE with -1 using fillna() and the subset parameter.
Create a list of StringIndexers by using list comprehension to iterate over each column in categorical_cols.
Apply fit() and transform() to the pipeline indexer_pipeline.
Drop the categorical_cols using drop() since they are no longer needed. Inspect the result data types using dtypes.
'''

# Code

# Replace missing values
df = df.fillna(-1, subset=['WALKSCORE', 'BIKESCORE'])

# Create list of StringIndexers using list comprehension
indexers = [StringIndexer(inputCol=col, outputCol=col+"_IDX")\
            .setHandleInvalid("keep") for col in categorical_cols]
# Create pipeline of indexers
indexer_pipeline = Pipeline(stages=indexers)
# Fit and Transform the pipeline to the original data
df_indexed = indexer_pipeline.fit(df).transform(df)

# Clean up redundant columns
df_indexed = df_indexed.drop(*categorical_cols)
# Inspect data transformations
print(df_indexed.dtypes)

'''result
<script.py> output:
    [('WALKSCORE', 'double'), ('BIKESCORE', 'double'), ('CITY_IDX', 'double'), ('LISTTYPE_IDX', 'double'), ('SCHOOLDISTRICTNUMBER_IDX', 'double'), ('POTENTIALSHORTSALE_IDX', 'double'), ('STYLE_IDX', 'double'), ('ASSUMABLEMORTGAGE_IDX', 'double'), ('ASSESSMENTPENDING_IDX', 'double')]
'''