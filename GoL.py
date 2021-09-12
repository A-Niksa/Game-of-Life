import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
import os

def Judge(A, i, j):
    n = A[i-1][j+1] + A[i][j+1] + A[i+1][j+1] + \
        A[i-1][j] + A[i+1][j] + \
        A[i-1][j-1] + A[i][j-1] + A[i+1][j-1]
    if A[i][j] == 0 and n == 3:
        A[i][j] = 1
    elif A[i][j] == 1 and (n == 2 or n == 3):
        pass
    else:
        A[i][j] = 0

def randMatrix(n): #a random n-by-b matrix
    A = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(0,1)
    return A

def matrixChecker(A):
    n = int(np.size(A) ** 0.5)
    A_bin = np.zeros([n+2,n+2])
    for i in range(1,n+1):
        for j in range(1,n+1):
            A_bin[i][j] = A[i-1][j-1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            Judge(A_bin,i,j)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1][j-1] = A_bin[i][j]  
    return A
    

def GoLRunner(n, m): #size of matrix(n)/number of steps(m)
    A = randMatrix(n)
    for i in range(1,m+1):
       A = matrixChecker(A)
       plt.imshow(A)
       plt.axis("off") # 'off' works too!
       plt.title(i)
       fname = "GoL - %s.png" % i
       plt.savefig(fname) 

# VARIABLES
n = 10 # matrix size
m = 25 # number of steps

# RUNNNG GoL
GoLRunner(n, m)

# GETTING A VIDEO EXPORT
test_img = cv2.imread("GoL - 1.png")
height, width, layers = test_img.shape
framesize = (width, height)
output = cv2.VideoWriter("GoL - Video.avi",cv2.VideoWriter_fourcc(*'DIVX'),1.5,framesize)
for fname in sorted(glob.glob("*.png"), key = os.path.getmtime):
    img = cv2.imread(fname)
    output.write(img)
    os.remove(fname)

output.release()