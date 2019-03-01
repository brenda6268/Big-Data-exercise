#Running a Cross-Validated Implicit ALS Model
'''
Now that we have several ALS models, each with a different set of hyperparameter values, we can train them on a training portion of the msd dataset using cross validation, and then run them on a test set of data and evaluate how well each one performs using the ROEM function discussed earlier. Unfortunately this takes too much time for this exercise, so it has been done separately. But for your reference you can evaluate your model_list using the following loop (we are using the msd dataset in this case):

# Split the data into training and test sets
(training, test) = msd.randomSplit([0.8, 0.2])

#Building 5 folds within the training set.
train1, train2, train3, train4, train5 = training.randomSplit([0.2, 0.2, 0.2, 0.2, 0.2], seed = 1)
fold1 = train2.union(train3).union(train4).union(train5)
fold2 = train3.union(train4).union(train5).union(train1)
fold3 = train4.union(train5).union(train1).union(train2)
fold4 = train5.union(train1).union(train2).union(train3)
fold5 = train1.union(train2).union(train3).union(train4)

foldlist = [(fold1, train1), (fold2, train2), (fold3, train3), (fold4, train4), (fold5, train5)]

# Empty list to fill with ROEMs from each model
ROEMS = []

# Loops through all models and all folds
for model in model_list:
    for ft_pair in foldlist:

        # Fits model to fold within training data
        fitted_model = model.fit(ft_pair[0])

        # Generates predictions using fitted_model on respective CV test data
        predictions = fitted_model.transform(ft_pair[1])

        # Generates and prints a ROEM metric CV test data
        r = ROEM(predictions)
        print ("ROEM: ", r)

    # Fits model to all of training data and generates preds for test data
    v_fitted_model = model.fit(training)
    v_predictions = v_fitted_model.transform(test)
    v_ROEM = ROEM(v_predictions)

    # Adds validation ROEM to ROEM list
    ROEMS.append(v_ROEM)
    print ("Validation ROEM: ", v_ROEM)
For purposes of walking you through the steps, the test predictions for 192 models have already been generated, and their ROEM has been calculated. They are found in the ROEMS list provided. Because a list isn't unique to Pyspark, and because numpy works really well with lists, we're going to use numpy here. Follow the instructions below to find the best ROEM and the model that provided it.

Instructions
100 XP

Import numpy
Extract the smallest ROEM from the ROEMS list provided using numpy.argmin(). The .argmin() method will return the index of the lowest value in the list provided. Call the result i and print i.
Use list slicing to find the value in the ROEMS list at index i.
'''

# Code
# Import numpy
import numpy

# Find the index of the smallest ROEM
i = numpy.argmin(ROEMS)
print ("Index of smallest ROEM:", i)

# Find ith element of ROEMS
print ("Smallest ROEM: ", ROEMS[i])

'''result
Index of smallest ROEM: 38
Smallest ROEM:  0.01980198019801982


'''
'''
#Extracting Parameters
You've now tested 192 different models on the msd dataset, and you found the best ROEM and it's respective model (model 38). You now need to exctract the hyperparameters. The model_list you created previously is provided here. It contains all 192 models you generated. Use the instructions below to extract the hyperparameters.

Instructions
100 XP
Use list slicing to extract model 38 from the model list. Call this model best_model.
Use the .get____() method to extract the following hyperparameter values:
Rank
MaxIter
RegParam
Alpha

'''

# Code
# Extract the best_model
best_model = model_list[38]

# Extract the Rank
print ("Rank: ", best_model.getRank())

# Extract the MaxIter value
print ("MaxIter: ", best_model.getMaxIter())

# Extract the RegParam value
print ("RegParam: ", best_model.getRegParam())

# Extract the Alpha value
print ("Alpha: ", best_model.getAlpha())

'''result
<script.py> output:
    Rank:  10
    MaxIter:  40
    RegParam:  0.05
    Alpha:  60.0
note:Looks like a low rank, a higher maxIter, 
a low regParam and a medium-high alpha is keeping the ROEM low. 
Because some of these values are on the high and low ends of the values we tried,
 it would be worth adding some additional values to test in our hyperparameter values, 
 and doing this step again, but for right now, you should understand the process.
'''