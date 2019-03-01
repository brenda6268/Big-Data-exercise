#Binary Model Performance
'''
You've already built several ALS models by now, so we won't do that again. An implicit ALS model has already been fitted to the binary ratings of the MovieLens dataset. Let's look at the binary_test_predictions from this model to see what we can learn.

The ROEM function has been defined for you. Feel free to run help(ROEM) in the console if you want more details on how to execute it!

Instructions
100 XP
Import the col function from the pyspark.sql.functions class.
Go ahead and take a look at binary_test_predictions using the .show() method to get an understanding of what the data looks like.
Call the ROEM function on the binary_test_predictions to evaluate the model's performance. Do you think it performed well?
Use the .filter() method to look at just user 42's predictions (col("userId") == 42). Do you notice anything?
'''

# Code
# Import the col function
from pyspark.sql.functions import col

# Look at the test predictions
binary_test_predictions.show()

# Evaluate ROEM on test predictions
ROEM(binary_test_predictions)

# Look at user 42's test predictions
binary_test_predictions.filter(col("userId") == 42).show()

'''result
<script.py> output:
    +------+-------+------+-----------+
    |userId|movieId|viewed| prediction|
    +------+-------+------+-----------+
    |    91|    148|     0|        0.0|
    |   601|    148|     0|        0.0|
    |   545|    148|     0|0.060729448|
    |   505|    148|     0|  0.2972868|
    |   526|    148|     0|        0.0|
    |   478|    148|     0|        0.0|
    |   106|    148|     0|        0.0|
    |   135|    148|     0|        0.0|
    |    78|    463|     0|0.050237626|
    |   259|    463|     0|0.027345931|
    |   127|    463|     0|0.016793307|
    |   502|    463|     0|0.019936942|
    |   441|    463|     0|0.002274946|
    |   664|    463|     0| 0.15109323|
    |   418|    463|     0|0.011756073|
    |   390|    463|     0|  0.3210355|
    |    32|    463|     0|0.018041197|
    |    58|    463|     0| 0.24846576|
    |   311|    463|     1|  1.0126673|
    |   471|    471|     0|  0.7693843|
    +------+-------+------+-----------+
    only showing top 20 rows
    
    ROEM: 0.07436376290899886
    +------+-------+------+-----------+
    |userId|movieId|viewed| prediction|
    +------+-------+------+-----------+
    |    42|    858|     0|  0.9915983|
    |    42|   3703|     0|  0.5134803|
    |    42|   2606|     0|        0.0|
    |    42|   6213|     0|0.008813023|
    |    42|   2342|     0|        0.0|
    |    42|  58107|     0|0.033887785|
    |    42|   6953|     0| 0.29286233|
    |    42|  41716|     0|        0.0|
    |    42|  49394|     0|0.021620607|
    |    42|   6509|     0|        0.0|
    |    42|   3512|     0|        0.0|
    |    42|   6810|     0|        0.0|
    |    42|  30749|     0| 0.60764235|
    |    42|  74282|     0|0.042640854|
    |    42|   2255|     0|        0.0|
    |    42|   3891|     0|        0.0|
    |    42|  31116|     0|        0.0|
    |    42|   2013|     0|  0.4043246|
    |    42|   3390|     0|        0.0|
    |    42|   1488|     0|        0.0|
    +------+-------+------+-----------+
    only showing top 20 rows

'''