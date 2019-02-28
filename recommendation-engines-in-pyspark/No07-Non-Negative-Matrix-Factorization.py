#Non-Negative Matrix Factorization
'''
It's possible for one matrix to have two equally close factorizations where one has all positive values, and the other has some negative values. The matrix M has been factored twice using two different factorizations. Take a look at each pair of factor matrices L and U, and W and H to see the differences. Then use their products to see that they produce essentially the same product.

Instructions
100 XP

Use the print command to view the L and U matrices. Notice that some values in matrices L and U are negative.
Use the print command to view the W and H matrices. Notice that all values in these two matrices are positive.
The L andU matrices and W and H matrices have been multiplied together to produce the LU and WH matrices respectively. Use the getRMSE(product_matrix, original_matrix) function to see how close LU is to M compared to how close WH is to M. Are they similar?
'''

# Code
# View the L, U, W, and H matrices.
print("Matrices L and U:") 
print(L)
print(U)

print("Matrices W and H:")
print(W)
print(H)


# Calculate RMSE between LU and M
print ("RMSE of LU: ", getRMSE(LU, M))

# Calculate RMSE between WH and M
print ("RMSE of WH: ", getRMSE(WH, M))




'''
Matrices L and U:
      0         1         2  3
0  1.00  0.000000  0.000000  0
1  0.01 -0.421053  0.098316  1
2  1.00  0.000000  1.000000  0
3  0.10  1.000000  0.000000  0
   0     1      2         3
0  1  2.00  1.000  2.000000
1  0 -0.19 -0.099 -0.198000
2  0  0.00  1.000 -1.000000
3  0  0.00  0.000  0.194947


Matrices W and H:
      0     1     2     3
0  2.61  0.24  0.00  0.12
1  0.00  0.05  0.02  0.17
2  1.97  0.00  0.58  0.83
3  0.05  0.00  0.00  0.00
      0     1     2     3
0  0.38  0.65  0.34  0.41
1  0.00  1.20  0.15  3.72
2  0.42  1.09  1.38  0.07
3  0.00  0.11  0.65  0.17



RMSE of LU:  0.072
RMSE of WH:  0.072

'''