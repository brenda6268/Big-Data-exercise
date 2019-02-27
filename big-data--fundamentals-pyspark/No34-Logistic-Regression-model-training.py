#Logistic Regression model training
'''
After creating labels and features for the data, we’re ready to build a model that can learn from it (training). But before you train the model, you'll split the combined dataset into training and testing dataset because it can assign a probability of being spam to each data point. We can then decide to classify messages as spam or not, depending on how high the probability.

In this final part of the exercise, you'll split the data into training and test, run Logistic Regression on the training data, apply the same HashingTF() feature transformation to get vectors on a positive example (spam) and a negative one (non-spam) and finally check the accuracy of the model trained.

Remember, you have a SparkContext sc available in your workspace, as well as the samples variable.

Instructions
100 XP

Split the combined data into training and test sets (80/20).
Train the training dataset using Logistic Regression's LBFGS algorithm.
Create a prediction label from the trained model on the test dataset.
Combine the labels in the test dataset with the labels in the prediction dataset.
Calculate the accuracy of the trained model using original and predicted labels on the labels_and_preds.

Hint
What method can split the RDD into training and test datasets?
Which method of LogisticRegressionWithLBFGS() can be used to train the model on the training dataset?
model has a predict() method that takes the test data as an input and generates labels.
Predicted labels are those that are obtained in the previous step.
The first index of the labels_and_preds is the original label and the second index is predicted by the model. You can use these two indexes to calculate MSE.
'''

# Code
# Split the data into training and testing
train_samples, test_samples = samples.randomSplit([0.8, 0.2])

# Train the model
model = LogisticRegressionWithLBFGS.train(train_samples)

# Create a prediction label from the test data
predictions = model.predict(test_samples.map(lambda x: x.features))

# Combine original labels with the predicted labels
labels_and_preds = test_samples.map(lambda x: x.label).zip(predictions)

# Check the accuracy of the model on the test data
accuracy = labels_and_preds.filter(lambda x: x[0] == x[1]).count() / float(test_samples.count())
print("Model accuracy : {:.2f}".format(accuracy))



'''
<script.py> output:
    Model accuracy : 0.82
'''