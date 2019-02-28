#RMSE As ALS Alternates
'''
As you know, ALS will alternate between the two factor matrices, adjusting their values each time to iteratively come closer and closer to approximating the original ratings matrix. This exercise is intended to illustrate this to you. Matrix T is a ratings matrix, and matrices F1, F2, F3, F4, F5, and F6 are the respective products of ALS after iterating 2, 3, 4, 5, and 6 times respectively. Follow the instructions below to see how the RMSE changes as ALS iterates.

Instructions
100 XP
Use the getRMSE(pred_matrix, actual_matrix) fucntion to calculate the RMSE of F1.
Put F2, F3, F4, F5, and F6 into one list called Fs.
Complete the getRMSEs(listOfPredMatrices, actualValues) function to calculate the RMSE of each matrix in the Fs list.
'''

#code
# Use the getRMSE(preds, actuals) function to calculate the RMSE of matrices T and F1.
getRMSE(F1, T)

# Create list of F2, F3, F4, F5, and F6
Fs = [F2, F3, F4, F5, F6]

# Calculate RMSE for F2, F3, F4, F5, and F6.
getRMSEs(Fs, T)

'''result
<script.py> output:
    F1:  2.4791263858912522
    F2: 0.4389326310548279
    F3: 0.17555006757053257
    F4: 0.15154042416388636
    F5: 0.13191130368008455
    F6: 0.04533823201006271

'''