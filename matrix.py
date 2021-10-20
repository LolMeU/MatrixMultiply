import numpy as np

#Transion matrix depending on what size it is this is a 8x8
M1 = np.array([[0.00, 0.50, 0.00, 0.25, 0.00, 0.00, 0.00, 0.00],
               [0.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.50, 0.00, 0.50, 0.00, 0.00, 0.00, 0.00],
               [0.50, 0.00, 1.00, 0.00, 0.25, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.25, 0.00, 0.50, 0.00, 0.50],
               [0.00, 0.00, 0.00, 0.00, 0.50, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 1.00, 0.50],
               [0.00, 0.00, 0.00, 0.00, 0.25, 0.00, 0.00, 0.00]])
print(M1)

#Transistion matrix for the wild
Mwild = np.array([[0.50, 0.25, 0.00, 0.125, 0.00, 0.00, 0.00, 0.00],
                  [0.25, 0.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
                  [0.00, 0.25, 0.50, 0.25, 0.00, 0.00, 0.00, 0.00],
                  [0.25, 0.00, 0.50, 0.50, 0.125, 0.00, 0.00, 0.00],
                  [0.00, 0.00, 0.00, 0.125, 0.50, 0.25, 0.00, 0.25],
                  [0.00, 0.00, 0.00, 0.00, 0.25, 0.50, 0.00, 0.00],
                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.25, 1.00, 0.25],
                  [0.00, 0.00, 0.00, 0.00, 0.125, 0.00, 0.00, 0.50]])
print(Mwild)

#raise the transistion matrix to a power(69)
Mdummy = np.linalg.matrix_power(M1, 69)
MdWild = np.linalg.matrix_power(Mwild, 69)
print(Mdummy)
print(MdWild)

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
M4 = MdWild.dot(M2)
print(M3)
print(M4)
print("Result for Lab:",int(M3[6]))
print("Result for Wild:",int((M4[6])/2))
