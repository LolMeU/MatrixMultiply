import numpy as np
import math

#Transion matrix depending on what size it is this is a 9x9
M1 = np.array([[0.00, 0.50, 0.00, 0.25, 0.00, 0.00, 0.00, 0.00, 0.00],
               [0.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.50, 0.00, 0.50, 0.00, 0.00, 0.00, 0.00, 0.00],
               [0.50, 0.00, 1.00, 0.00, 0.25, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.25, 0.00, 0.50, 0.00, 0.50, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.50, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.00, 0.50, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.25, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 1.00]])
print(M1)

#Transistion matrix for the wild
Mwild = np.array([[0.50, 0.25, 0.00, 0.125, 0.00, 0.00, 0.00, 0.00, 0.00],
                  [0.25, 0.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
                  [0.00, 0.25, 0.50, 0.25, 0.00, 0.00, 0.00, 0.00, 0.00],
                  [0.25, 0.00, 0.50, 0.50, 0.125, 0.00, 0.00, 0.00, 0.00],
                  [0.00, 0.00, 0.00, 0.125, 0.50, 0.25, 0.00, 0.25, 0.00],
                  [0.00, 0.00, 0.00, 0.00, 0.25, 0.50, 0.00, 0.00, 0.00],
                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.25, 0.50, 0.25, 0.00],
                  [0.00, 0.00, 0.00, 0.00, 0.125, 0.00, 0.00, 0.50, 0.00],
                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.50, 0.00, 1.00]])
print(Mwild)

#Raise the transistion matrix to a power(69)
Mdummy = np.linalg.matrix_power(M1, 69)
MdWild = np.linalg.matrix_power(Mwild, 69)

#Check if 69 is steady state
Mdummy2 = np.linalg.matrix_power(M1, 70)
MdWild2 = np.linalg.matrix_power(Mwild, 70)

print(Mdummy)
print(MdWild)

#The initial matrix assuming 100 were in room 1
M2 = np.array([[100],
               [0],
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
M4 = MdWild.dot(M2)
M5 = Mdummy2.dot(M2)
M6 = MdWild2.dot(M2)

print(M5)
print(M6)
print(M3)
#Print the sum of the first row of M3
print("Sum of Values Lab:", int(M3.sum(axis=0)))
print(M4)
#Print the sum of the first row of M4
print("Sum of Values Wild:", int(M4.sum(axis=0)))
print("Result for Lab:",math.floor(M3[8]))
print("Result for Wild:",math.floor((M4[8])))
