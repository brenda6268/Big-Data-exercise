#Estimating Recommendations
'''
Use your knowledge of matrix multiplication to determine which movie will have the highest recommendation for User_3. The ratings matrix has been factorized into U and P with ALS.

step1 View the left factor matrix, U, using the print function.

step2 Did you see anything interesting about User_3? Now inspect the right factor matrix, P. Use the print function.

step3 Looking at U and P, which movie do you think will have the highest recommendation for User_3.
Multiply U and P using numpy's matmul to obtain recommendations. Call thisUP.
Complete the code to print UP.
'''

# step1 code
print (U)

'''result
  U_LF_1   ...    U_LF_4
User_1    0.80   ...       0.8
User_2    0.40   ...       0.2
User_3    0.05   ...       2.2
User_4    0.30   ...       0.2
User_5    0.10   ...       0.0
User_6    0.00   ...       0.5
User_7    0.01   ...       0.4
User_8    0.90   ...       1.0
User_9    1.00   ...       0.2

[9 rows x 4 columns]
'''

# Step2 code
# View right factor matrix
print (P)

'''result
 Movie_1   ...     Movie_4
P_LF_1      0.5   ...        1.10
P_LF_2      0.2   ...        0.01
P_LF_3      0.3   ...        0.90
P_LF_4      1.0   ...        0.89

[4 rows x 4 columns]
'''

# Step3 code
# Multiply factor matrices
UP = np.matmul(U,P)

# Convert to pandas DataFrame
print (pd.DataFrame(UP, columns = P.columns, index = U.index))

'''result

 Movie_1   ...     Movie_4
User_1    1.292   ...      1.8621
User_2    0.420   ...      0.6721
User_3    2.648   ...      2.0430
User_4    0.412   ...      0.6881
User_5    0.620   ...      0.9350
User_6    0.626   ...      0.8053
User_7    0.607   ...      0.9612
User_8    1.590   ...      1.8870
User_9    1.112   ...      1.3340

[9 rows x 4 columns]


'''