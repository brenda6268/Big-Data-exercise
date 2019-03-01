#Generate predictions and calculate RMSE
'''
Now that we have a model that is trained on our data and tuned through cross validation, we can see how it performs on the test dataframe. To do this, we'll calculate the RMSE. As a side note, the generation of test predictions takes more than a few minutes with this dataset. For this reason, the test predictions have been generated already and are provided here as a dataframe called test_predictions. For your reference, they are generated using this code: test_predictions = best_model.transform(test).

Instructions
100 XP
The dataframe test_predictions contains predictions that our cross-validated ALS model generated using the test set that we created previously. Use the .show() method to take a look at it and see if the predictions seem close.
Use the evaluator that you built previously to calculate the RMSE by calling the .evaluate() method on the test_predictions generated. Call this "RMSE"
'''

# Code
# View the predictions 
test_predictions.show()

# Calculate and print the RMSE of the test_predictions
RMSE = evaluator.evaluate(test_predictions)
print (RMSE)

'''result
+------+-------+------+------------------+
|userId|movieId|rating|        prediction|
+------+-------+------+------------------+
|   380|    463|   3.0| 4.093334993256898|
|   460|    471|   5.0| 4.789751482535894|
|   440|    471|   3.0| 2.440344619907418|
|   306|    471|   3.0|3.3247629567900976|
|    19|    471|   3.0| 3.067333162723295|
|   299|    471|   4.5| 5.218491499885204|
|   537|    471|   5.0|  5.69083471617962|
|   241|    471|   4.0| 3.816546176254299|
|    23|    471|   3.5| 2.539020466532909|
|   195|    471|   3.0| 3.355342979133588|
|   487|    471|   4.0| 3.105186392315445|
|   242|    471|   5.0| 5.893115933597325|
|    30|    471|   4.0| 4.017221049024606|
|   516|   1088|   3.0|3.3911144131643005|
|   111|   1088|   3.5| 4.504826156475481|
|    57|   1088|   4.0| 3.024549429857915|
|    54|   1088|   5.0| 5.235519746597422|
|    19|   1088|   3.0|  3.70884171609874|
|   387|   1088|   4.0| 4.070842875474657|
|   514|   1088|   3.0| 2.313176685047038|
+------+-------+------+------------------+
only showing top 20 rows

0.6332304339145925

note:An RMSE of 0.633 means that :
on average the model predicts 0.633 above or below values of the original ratings matrix.

'''