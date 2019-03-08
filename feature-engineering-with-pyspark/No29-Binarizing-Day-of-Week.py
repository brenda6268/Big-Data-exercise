#Binarizing Day of Week
'''
In a previous video, we saw that it was very unlikely for a home to list on the weekend. Let's create a new field that says if the house is listed for sale on a weekday or not. In this example there is a field called List_Day_of_Week that has Monday is labeled 1.0 and Sunday is 7.0. Let's convert this to a binary field with weekday being 0 and weekend being 1. We can use the pyspark feature transformer Binarizer to do this.

Instructions
100 XP

Import the feature transformer Binarizer from pyspark and the ml.feature module.
Create the transformer using Binarizer() with the threshold for setting the value to 1 as anything after Friday, 5.0, then set the input column as List_Day_of_Week and output column as Listed_On_Weekend.
Apply the binarizer transformation on df using transform().
Verify the transformation worked correctly by selecting the List_Day_of_Week and Listed_On_Weekend columns with show().
'''

# Code
# Import transformer
from pyspark.ml.feature import Binarizer

# Create the transformer
binarizer = Binarizer(threshold=5.0, inputCol='List_Day_of_Week', outputCol='Listed_On_Weekend')

# Apply the transformation to df
df = binarizer.transform(df)

# Verify transformation
df[['List_Day_of_Week' , 'Listed_On_Weekend']].show()

'''result
<script.py> output:
    +----------------+-----------------+
    |List_Day_of_Week|Listed_On_Weekend|
    +----------------+-----------------+
    |             6.0|              1.0|
    |             1.0|              0.0|
    |             1.0|              0.0|
    |             5.0|              0.0|
    |             2.0|              0.0|
    |             1.0|              0.0|
    |             4.0|              0.0|
    |             7.0|              1.0|
    |             4.0|              0.0|
    |             6.0|              1.0|
    |             5.0|              0.0|
    |             4.0|              0.0|
    |             7.0|              1.0|
    |             1.0|              0.0|
    |             4.0|              0.0|
    |             7.0|              1.0|
    |             7.0|              1.0|
    |             5.0|              0.0|
    |             6.0|              1.0|
    |             5.0|              0.0|
    +----------------+-----------------+
    only showing top 20 rows

'''