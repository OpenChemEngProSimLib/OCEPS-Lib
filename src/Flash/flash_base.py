from maingopy import *
import numpy as np

class Flash(MAiNGOmodel):
    class psi_class:
        def __init__(self):
            self.z = None
            self.k = None
            
        def set_values(self, z, k):
            self.z = np.array(z)
            self.k = np.array(k)
            
        def f_psi(self, psi): 
            return (np.sum((self.z*(1 - self.k))/(1+psi*(self.k - 1))))**2

    def __init__(self):
        MAiNGOmodel.__init__(self) # Should be there for technical reasons
        self.ext = self.psi_class()
    
    def get_variables(self):
        return [OptimizationVariable(Bounds(0,1), VT_CONTINUOUS, "psi")]
    
    def get_initial_point(self):
        return [0.5]

    def evaluate(self, vars):
        result = EvaluationContainer()
        result.objective = self.ext.f_psi(vars[0])
        return result

def solve_flash(z, k):
    myModel = Flash()
    myModel.ext.set_values(z, k)
    myMAiNGO = MAiNGO(myModel)
    myMAiNGO.read_settings("")
    myMAiNGO.set_option("loggingDestination", LOGGING_NONE)
    myMAiNGO.set_option('writeResultFile', False)
    myMAiNGO.solve()
    return myMAiNGO.get_solution_point()
