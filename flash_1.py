from maingopy import *

from math import pi
import numpy as np

class psi_class:
    def __init__(self, z, k):
        self.z = np.array(z)  # Composition for multiple components
        self.k = np.array(k)  # K-values for multiple components

    def f_psi(self, psi):
        return np.sum((self.z * (1 - self.k)) / (1 + psi * (self.k - 1)))

#####################################################
class Flash(MAiNGOmodel):
    def __init__(self):
        MAiNGOmodel.__init__(self) # Should be there for technical reasons
        z = [0.2, 0.8] # Composition
        k = [1 , 0.5]  # Equilibrium
        self.ext = psi_class(z, k)
    
    # We need to implement the get_variables functions for specifying the optimization variables
    def get_variables(self):

        variables = [OptimizationVariable(Bounds(0,1), VT_CONTINUOUS, "Objective") ]    
        return variables

    def get_initial_point(self):
        initialPoint = [0.5] # Initial value of psi = 0.5
        return initialPoint


    def evaluate(self, vars):
        # Create copies of the variables with nicer names
        psi = vars[0]
        # Any variables defined here are intermediates that are not optimization variables.
        temp1 = self.ext.f_psi(psi) # psi function
        
        # The objective and constraints are returned in an EvaluationContainer
        result = EvaluationContainer()
        
        # Function psi
        result.objective = temp1
        
        # Additional output can be used to access intermediate variables after a problem has been solved.
        result.output = [OutputVariable("Value of psi: ", temp1)]

        return result

#####################################################
# To work with the problem, we first create an instance of the model.
myModel = Flash()

# We then create an instance of MAiNGO, the solver, and hand it the model.
myMAiNGO = MAiNGO(myModel)

fileName = ""
myMAiNGO.read_settings(fileName) # If fileName is empty, MAiNGO will attempt to open MAiNGOSettings.txt

maingoStatus = myMAiNGO.solve() 
#print(maingoStatus)
