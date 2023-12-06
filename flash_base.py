from maingopy import *
#from math import pi
import numpy as np

#####################################################
# Main Flash Code
class Flash(MAiNGOmodel):
    class psi_class:
        def __init__(self):
            self.z = None # Composition
            self.k = None # K - equilibrium
            
        def set_values(self, z, k):
            self.z = np.array(z)
            self.k = np.array(k)
            
        def f_psi(self, psi): # Function of psi -> 0 
            a = (np.sum((self.z*(1 - self.k))/(1+psi*(self.k - 1))))**2
            return a

    def __init__(self):
        MAiNGOmodel.__init__(self) # Should be there for technical reasons
        self.ext = self.psi_class()
    
    # We need to implement the get_variables functions for specifying the optimization variables
    def get_variables(self):
        variables = [OptimizationVariable(Bounds(0,1), VT_CONTINUOUS, "psi") ]    
        return variables

    def get_initial_point(self):
        initialPoint = [0.5] # Initial value of psi = 0.5
        return initialPoint

    def evaluate(self, vars):
        # Create copies of the variables with nicer names
        psi = vars[0]
        # Any variables defined here are intermediates that are not optimization variables.
        #temp1 =  # psi function
        
        # The objective and constraints are returned in an EvaluationContainer
        result = EvaluationContainer()
        
        # Function psi
        result.objective = self.ext.f_psi(psi)
        
        return result
#####################################################

def solve_flash(z, k):
    # To work with the problem, we first create an instance of the model.
    myModel = Flash()

    # Set the values of z and k
    myModel.ext.set_values(z, k)

    # We then create an instance of MAiNGO, the solver, and hand it the model.
    myMAiNGO = MAiNGO(myModel)

    fileName = ""
    myMAiNGO.read_settings(fileName) # If fileName is empty, MAiNGO will attempt to open MAiNGOSettings.txt
    myMAiNGO.set_option("loggingDestination", LOGGING_NONE) # Not generate a logfile
    myMAiNGO.set_option('writeResultFile', False) # Not generate a txt results file
    
    myMAiNGO.solve()
    maingoStatus = myMAiNGO.get_solution_point()
    return maingoStatus

# Now you can call the function solve_flash with different values of z and k
status = solve_flash([0.1,0.2,0.3,0.4], [4.2,1.75, 0.74, 0.34])
print(status)
#print(status)
