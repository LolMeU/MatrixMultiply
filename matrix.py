import numpy as np

#Transion matrix depending on what size it is this is a 8x8
M1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]])
print(M1)

#raise the transistion matrix to a power(69)
Mdummy = np.linalg.matrix_power(M1, 69)
print(Mdummy)

#The initial matrix
M2 = np.array([[100],
               [0],
               [0],
               [0],
               [0],
               [0],
               [0],
               [0]])
print(M2)

#Multiply them together to get the steady state
M3 = Mdummy.dot(M2)
print(M3)
